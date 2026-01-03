from odoo import models, fields

class TpReunion(models.Model):
    _name = "tp.reunion"
    _description = "Réunion TP"

    name = fields.Char(string="Sujet de la réunion", required=True)
    responsable = fields.Char(string="Responsable")
    date = fields.Datetime(string="Date et Heure", default=fields.Datetime.now)
    lieu = fields.Char(string="Lieu")
    statut = fields.Selection([
        ("brouillon", "Brouillon"),
        ("planifiee", "Planifiée"),
        ("terminee", "Terminée"),
        ("annulee", "Annulée"),
    ], string="Statut", default="brouillon")
    description = fields.Text(string="Ordre du jour")
