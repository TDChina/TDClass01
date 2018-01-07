# -*- coding: utf-8 -*-
import math
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import Qt, QUrl, QObject, pyqtSlot, QCoreApplication
from PyQt5.QtGui import QGuiApplication


class PrimeFactor(QObject):

    @pyqtSlot(str, result=str)
    def analyze(self, number):
        try:
            number = int(number)
            if number < 2:
                return u"请输入一个大于1的整数"
        except ValueError:
            return u"输入无效"
        result = ' * '.join([str(prime) for prime in self.prime_factor(number)])
        return "{number} = {result}".format(**locals())

    def prime_factor(self, number, start=2):
        for prime in range(start, int(math.sqrt(number) + 1)):
            if number % prime == 0:
                return [prime] + self.prime_factor(number / prime, prime)
        return [] if number == 1 else [int(number)]


if __name__ == "__main__":
    import os
    import sys

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QGuiApplication(sys.argv)
    view = QQuickView()
    prime_factor = PrimeFactor()
    context = view.rootContext()
    context.setContextProperty("primeFactor", prime_factor)
    view.engine().quit.connect(app.quit)
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__), 'main.qml')))
    view.setTitle(u"质因数分解")
    view.show()
    sys.exit(app.exec_())
