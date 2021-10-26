# Copyright 2021 Camptocamp (https://www.camptocamp.com).
# @author Iván Todorovich <ivan.todorovich@camptocamp.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SeIndexObsoleteBinding(models.Model):
    """Search Engine Obsolete Binding

    When bound records are deleted, their IDs are temporarily stored here
    until the next synchronization.
    """

    _name = "se.index.obsolete.binding"
    _description = "Search Engine Obsolete Binding"

    index_id = fields.Many2one(
        "se.index",
        string="Index",
        ondelete="cascade",
        required=True,
    )
    res_id = fields.Integer(string="Record ID", required=True)
