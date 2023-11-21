################################################################################
# SMTP configuration settings.
################################################################################
smtp = {
    'username': '',
    'password': '',
    'host': '',
    'port': 587,
    'from_email': '',
}

################################################################################
# This the secret santa letter template that is used to send everyone the email.
# Note that {santa} and {recipient} are automatically replaced by the secret
# santa's name, and his/her recipient of their gift.
################################################################################
email_template = {
    'from_name': 'Secret Santa',
    'from_email': smtp['from_email'],
    'subject': 'Noel des 4As',
    'body': """
Ho Ho Ho!

Noël arrive à grands pas et je ne vais avoir le temps de préparer des cadeaux pour tout le monde.
{santa}, aide moi et offre un cadeau à {recipient}!

Un grand merci et un Joyeux Noël à toi!

Le père noël
"""
}

################################################################################
# The complete list of all the secret santa's and their email addresses.
################################################################################
santas = {
    'Frédéric': 'flegrand31@gmail.com',
    'Tom': 'tom.renaudin@etu.ec-lyon.fr',
    'Pierre-Louis': 'pierre-louis.mourey@etu.ec-lyon.fr',
    'Martin': 'martin.donnay@etu.ec-lyon.fr',
    'Paul': 'paul.marin@etu.ec-lyon.fr',
    'Théo': 'theo.denis-de-senneville@etu.ec-lyon.fr',
    'Alix': 'alix.macgregor@etu.ec-lyon.fr',
    'Gaspard': 'gaspard.leridon@etu.ec-lyon.fr',
    'Wenceslas': 'wenceslas.martinez@etu.ec-lyon.fr',
    'Léonie': 'leonie.mouchel@etu.ec-lyon.fr',
    'Antonin': 'antonin.delorme@etu.ec-lyon.fr'
}

################################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values).
#
# If there are no incompatibles, leave this dictionary empty.
################################################################################
incompatibles = {

}

################################################################################
# DON'T PEAK INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
################################################################################
secret_santa_record_file = 'secret-santa-record-file.txt'
