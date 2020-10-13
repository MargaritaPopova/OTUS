from flask import Blueprint, render_template

portfolio_app = Blueprint("portfolio_app", __name__)


def get_menu():
    menu = [
        {'url': f'/portfolio/certificates', 'name': 'Certificates'},
        {'url': f'/portfolio/projects', 'name': 'Projects'},
    ]
    return menu


@portfolio_app.route("/")
def portfolio():
    context = {
        'main_message': 'My Portfolio',
        'main_text': 'Welcome to my portfolio website! Here you can take a look at projects I '
                     'took part in and check out my certificates from online courses I completed'
    }
    return render_template("portfolio/main.html", menu=get_menu(), context=context)


@portfolio_app.route("/certificates")
def certificates():
    context = {
        'main_message': 'My Certificates',
        'certif_list': [
            {'url': 'https://www.coursera.org/account/accomplishments/certificate/FBRH36YMKU4N',
             'name': 'Web Technologies and Django'},
            {'url': 'https://geekbrains.ru/certificates/453624', 'name': 'HTML5 & CSS3'},
            {'url': 'https://geekbrains.ru/certificates/554013', 'name': 'Databases for Web'},
            {'url': 'https://geekbrains.ru/certificates/585182', 'name': 'Yii2 Framework'},
            {'url': 'https://geekbrains.ru/certificates/523916', 'name': 'A Quickstart to Git'},
        ]
    }
    return render_template("portfolio/certif.html", menu=get_menu(), context=context)


@portfolio_app.route("/projects")
def projects():
    context = {
        'main_message': 'My Projects',
        'proj_list': [
            {'url': 'https://github.com/fortys1xandtwo/SimpleVotings08',
             'name': 'Simple Votings'},
            {'url': 'https://prom.informatics.ru/2020/online/s101/', 'name': 'Minute of Fame'},
        ]
    }
    return render_template("portfolio/proj.html", menu=get_menu(), context=context)