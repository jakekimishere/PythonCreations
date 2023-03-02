#ifndef PASSWORDCHECK_H
#define PASSWORDCHECK_H

#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui { class passwordCheck; }
QT_END_NAMESPACE

class passwordCheck : public QWidget
{
    Q_OBJECT

public:
    passwordCheck(QWidget *parent = nullptr);
    ~passwordCheck();

private slots:
    void on_enterButton_clicked();

    void on_hashButton_clicked();

    void on_helpButton_pressed();

    void on_exitButton_clicked();

    void on_hashBox_activated(int index);

private:
    Ui::passwordCheck *ui;
    bool requirementCheck(QString password);
};
#endif // PASSWORDCHECK_H
