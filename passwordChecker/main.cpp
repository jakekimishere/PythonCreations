#include "passwordcheck.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    passwordCheck w;
    w.show();
    return a.exec();
}
