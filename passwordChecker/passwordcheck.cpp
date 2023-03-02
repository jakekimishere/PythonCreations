#include "passwordcheck.h"
#include "ui_passwordcheck.h"

passwordCheck::passwordCheck(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::passwordCheck)
{
    ui->setupUi(this);
}

passwordCheck::~passwordCheck()
{
    delete ui;
}

bool passwordCheck::requirementCheck(QString password){
    // Password must be at least 8 characters long
    if (password.length() < 8) {
       return false;
    }
    // Password must contain at least one uppercase letter, one lowercase letter, and one digit
    bool hasUpperCase = false;
    bool hasLowerCase = false;
    bool hasDigit = false;

    for (const QChar& c : password) {
        if (c.isUpper()) {
            hasUpperCase = true;
        } else if (c.isLower()) {
            hasLowerCase = true;
        } else if (c.isDigit()) {
            hasDigit = true;
        }

        if (hasUpperCase && hasLowerCase && hasDigit) {
            return true;
        }
    }

    return false;
}

void passwordCheck::on_enterButton_clicked()
{
    QString password = ui->insertPassword->text();

        if (requirementCheck(password)) {
            // Password meets complexity requirements
            ui->reqResult->setText("Password works yayayaya.");
        } else {
            // Password does not meet complexity requirements
            ui->reqResult->setText("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.");
        }
}


void passwordCheck::on_hashButton_clicked()
{

}


void passwordCheck::on_helpButton_pressed()
{

}


void passwordCheck::on_exitButton_clicked()
{

}


void passwordCheck::on_hashBox_activated(int index)
{

}

