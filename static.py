class Foo(object):
    counter = 0
    widht = 0
    rIndex = 1
    cIndex = 0
    workSheetIndex = 1

    def __call__(self):
        Foo.counter += 1
        print(Foo.counter)  # Buna bakılacak

    def rowIndex(self):
        return (Foo.rIndex)

    def rowIndexIncrease(self):
        Foo.rIndex += 1
        return (Foo.rIndex)

    def columnIndex(self):
        return (Foo.cIndex)

    def columnIndexDecrease(self):
        Foo.cIndex -= 1
        return (Foo.cIndex)

    def columnIndexIncrease(self):
        if Foo.cIndex % 7 == 0 and Foo.cIndex != 0:
            Foo.cIndex = 0
            Foo.rowIndexIncrease(self)
            # print(Foo.cIndex)
        Foo.cIndex += 1
        return (Foo.cIndex)

    def workSheetIndexIncrease(self):
        Foo.workSheetIndex += 1
        return (Foo.workSheetIndex)
