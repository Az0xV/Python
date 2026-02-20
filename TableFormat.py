# Comment this script
import colorama

colorama.init()

class TableService:
    def __init__(self):
        self.columns = []
    
    def displayTable(self):
        if not self.columns:
            return

        widthForColumn = []
        for column in self.columns:
            widthForColumn.append((column.name, column.length, column.values))
        
        dashes = ""

        for dash in widthForColumn:
            dashes += "-" * (dash[1]+6)
        print(dashes)

        for width in widthForColumn:
            print(" | " + width[0] + " | ",end="")
        print()
        
        # Find the maximum number of values across all columns
        max_rows = max(len(column.values) if column.values else 0 for column in self.columns)

        for row in range(max_rows):
            for width in widthForColumn:
                value = 0
                roundValue = 2
                try:
                    value = width[2][row]
                    if isinstance(value,(int,float)):
                        value = round(width[2][row], roundValue)
                except IndexError:
                    value = "..."

                length = len(str(value))
                fit = width[1] - length

                while (fit < 0):
                    if isinstance(value,(int,float)):
                        roundValue -= 1
                        if roundValue >= 0:
                            value = round(value, roundValue)
                            fit = length - width[1]
                            continue
                    value = str(value)[:width[1]-1] + "+"
                    fit = 0
                value = str(value) + " "*fit
                color = colorama.Fore.CYAN
                if row%2==1: color = colorama.Fore.YELLOW
                print(f"{color} | {value} | {colorama.Fore.RESET}",end="")
            print()
        print(dashes)
        
    def addColumn(self, column):
        if not isinstance(column, TableColumn):
            raise ValueError("Invalid column type.")
        self.columns.append(column)

class TableColumn:
    def __init__(self, name = "", length = 0, values = None):
        self.name = name
        if length < len(name):
            self.length = len(name)
        else:
            self.length = length
            self.name = self.name.ljust(self.length)
        self.values = values