Indoguna UDF Company
====================

Deskripsi
---------
Modul ini menambahkan field dan tampilan tambahan pada model perusahaan dan pengguna di Odoo.
Fokus utamanya adalah:

- Penyimpanan konfigurasi koneksi ERP/SAP pada perusahaan.
- Penyimpanan atribut internal pengguna (departemen dan level).
- Penambahan tab konfigurasi langsung di form bawaan Odoo.

Informasi Modul
---------------
- Nama modul: ``igu_company``
- Nama aplikasi (manifest): ``Indoguna UDF Company``
- Versi: ``18.1``
- Kategori: ``SAP Integration``
- Dependensi: ``base``

Ruang Lingkup Perubahan
-----------------------
1. Inherit model ``res.company``
2. Inherit model ``res.users``
3. Inherit view form ``res.company``
4. Inherit view form ``res.users``

Model: res.company
------------------
Model ``res.company`` ditambah field untuk konfigurasi integrasi ERP/SAP dan kebutuhan accounting.

Field yang ditambahkan:

- ``company_code`` (Char): kode/ttd kwitansi.
- ``company_bp_code`` (Char): company BP code.
- ``erp_type`` (Selection): jenis ERP (``tradeerp``, ``sap``, ``odoo12``), default ``sap``.
- ``code_base`` (Char): code base.
- ``server`` (Char): IP/URL server SAP B1.
- ``db_name`` (Char): nama database/app SAP B1.
- ``db_usr`` (Char): user database SAP B1.
- ``db_pass`` (Char): password database SAP B1.
- ``server2`` (Char): IP/URL server ke-2 (WEB).
- ``db_name2`` (Char): nama database/app ke-2 (WEB).
- ``db_usr2`` (Char): user database ke-2 (WEB).
- ``db_pass2`` (Char): password database ke-2 (WEB).
- ``sapweb`` (Char): URL SAP web.
- ``sapuser`` (Char): user SAP Service Layer.
- ``sappassword`` (Char): password SAP Service Layer.
- ``sapsl`` (Char): endpoint SAP Service Layer.
- ``webapi`` (Char): URL web REST API.
- ``rek`` (Char): nomor rekening.
- ``loc`` (Char): lokasi.
- ``kwitansi`` (Char): penanda ttd kwitansi.
- ``igu_logo`` (Binary): logo perusahaan.

Perubahan tampilan ``res.company``:

- Tab ``SAP DB Connection``
  - Grup ``SAP B1 DB Setting``
  - Grup ``SAP WEB DB Setting``
- Tab ``SAP Setting``
- Tab ``Accounting Setting``

Model: res.users
----------------
Model ``res.users`` ditambah field untuk identitas internal pengguna.

Field yang ditambahkan:

- ``igu_dept`` (Selection): departemen internal, default ``OTHER``.
- ``igu_group`` (Char): internal group, default ``Finance``.
- ``state`` (Char): state.
- ``igu_lvl`` (Selection): level pengguna, default ``user``.

Perubahan tampilan ``res.users``:

- Tab ``Indoguna Internal``
  - Grup ``Setting``
  - Menampilkan field ``igu_dept`` dan ``igu_lvl``.

Cara Instalasi
--------------
1. Pastikan modul berada pada path addons Odoo.
2. Update daftar aplikasi.
3. Cari aplikasi ``Indoguna UDF Company``.
4. Klik Install.

Setelah terpasang:

- Buka menu Settings > Companies untuk mengisi parameter SAP/ERP.
- Buka user form untuk mengisi data departemen dan level internal.

File yang Dimuat Manifest
-------------------------
Data XML yang dimuat pada instalasi:

- ``init_models/inherit_res_company.xml``
- ``init_models/inherit_res_users.xml``

Catatan
-------
- File ``views/views.xml`` dan ``views/templates.xml`` saat ini berisi template komentar bawaan dan tidak dimuat di manifest.
- Nilai field sensitif seperti password sebaiknya dibatasi aksesnya melalui aturan security (ir.model.access/rules dan group) sesuai kebijakan internal.
