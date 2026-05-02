# -*- coding: utf-8 -*-

from odoo import models, fields, api

class IuCompanyGroup(models.Model):
	_inherit="res.company"

## Optional Code for future use (Multi Company)
	company_code = fields.Char("Company Internal Code")
	company_bp_code = fields.Char("Company Partner Code")

	code_base   = fields.Char("Company Code Base (Financial Report)")
	
 


# DB B1
	server      = fields.Char("IP / URL Server")
	db_name     = fields.Char("DB Name / Apps Name")
	db_usr      = fields.Char("DB User / User")
	db_pass     = fields.Char("DB Password / User")

 #SAP DB WEB
	server2     = fields.Char("IP / URL Server 2 ")
	db_name2    = fields.Char("DB Name / Apps Name 2 ")
	db_usr2     = fields.Char("DB User / User 2 ")
	db_pass2    = fields.Char("DB Password / User 2")

 #PostgreSQL DB 
	server3     = fields.Char("IP / URL Server 3 ")
	db_name3    = fields.Char("DB Name / Apps Name 3 ")
	db_usr3     = fields.Char("DB User / User 3 ")
	db_pass3    = fields.Char("DB Password / User 3")


# WEB APPLICATION URL
	sapweb      = fields.Char("  WEB URL  (if Any)  ")
	webapi	 	= fields.Char("WEB FastAPI-Jasper API URL")
	urllogo 	= fields.Char("URL Logo (if Any)")
# Service Layer / Web API
	sapuser		= fields.Char("SAP User")
	sappassword	= fields.Char("SAP PAssword")
	sapsl 		= fields.Char("SAP Service Layer URL")
	 

 
