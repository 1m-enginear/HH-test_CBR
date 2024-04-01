'''
Семенов А.С.
Тестовое задание.
'''
import xml.etree.ElementTree as ET

def check_xml_structure(xml_file):
    '''
    Функция проверки структуры XML файла
    Принимает:
    xml_file - путь к файлу XML (str)
    Возвращает:
    Результат проверки (bool).
    True - файл соответствует структуре
    False - файл не соответствует структуре
    '''
    
    # Открываем файл
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # Если корневой элемент не 'Balance'
        if root.tag != 'Balance':
            print ('Корневой элемент Balance не обнаружен!')
            return False # Возвращем False

        else:
            
            # Цикл по элементам
            for element in root:
                
                # Проверяем элемнты 'Oper'
                if element.tag != "Oper":
                    print(f"Обнаружен элемент, не соответствующий ожидаемой структуре: {element.tag}")
                    return False
                else:
                    
                    # Проверяем наличие атрибутов
                    atrributes = element.attrib
                    atrributes = list(atrributes.keys())
                    if atrributes != ['data', 'corAcc', 'dbt', 'cdt']:
                        print(f"Отсутствует атрибут в элементе. Ожидается ['data', 'corAcc', 'dbt', 'cdt'], получено: {atrributes}")
                        return False
            
            # Возвращаем True, ошибок не найдено
            return True
        
    # При ошибке парсинга возвращаем False
    except ET.ParseError:
        return False

if __name__ == "__main__":
    
    # Путь к файлу XML
    xml_file = "./Balance.xml"
    
    # Вызов функции
    valid_structure = check_xml_structure(xml_file)
    
    # Вывод результата
    if valid_structure:
        print("Структура XML-файла верна")
    else:
        print("Структура XML-файла не верна")