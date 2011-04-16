REQUIRED_FIELDS = ['title',
                   'description',
                   'publication_date',
                   'north_bounding_latitude',
                   'south_bounding_latitude',
                   'east_bounding_longitude',
                   'west_bounding_longitude',
                   'metadata_contact_org_name',
                   'metadata_contact_email',]

ONE_OF_FIELDS = [['originator_contact_org_name', 'originator_contact_person_name', 'originator_contact_position_name'],
                 ['originator_contact_email', 'originator_contact_phone']]

OPTIONAL_FIELDS = ['resource_type',
                   'keywords_thematic',
                   'keywords_spatial',
                   'keywords_temporal',
                   'originator_contact_street_address',
                   'originator_contact_city',
                   'originator_contact_state',
                   'originator_contact_zip',
                   'originator_contact_fax',
                   'originator_contact_url',
                   'bibliographic_citation',
                   'elevation_units',
                   'temporal_start_date',
                   'temporal_end_date',
                   'resource_languages',
                   'resource_id',
                   'resource_url',
                   'resource_access_instruction',
                   'resource_quality_statement',
                   'resource_constraints_statement',
                   'resource_lineage_statement',
                   'distributor_contact_org_name',
                   'distributor_contact_person_name',
                   'distributor_contact_position_name',
                   'distributor_contact_street_address',
                   'distributor_contact_city',
                   'distributor_contact_state',
                   'distributor_contact_zip',
                   'distributor_contact_email',
                   'distributor_contact_phone',
                   'distributor_contact_fax',
                   'distributor_contact_url',
                   'metadata_date',
                   'metadata_language',
                   'metadata_uuid',
                   'metadata_contact_person_name',
                   'metadata_contact_position_name',
                   'metadata_contact_street_address',
                   'metadata_contact_city',
                   'metadata_contact_state',
                   'metadata_contact_zip',
                   'metadata_contact_phone',
                   'metadata_contact_fax',
                   'metadata_contact_url',
                   'related_resource']

OPTIONAL_ONE_OF_FIELDS = [['datum_elevation', 'surface_elevation'],
                          ['extent_maximum', 'interval_depth_top'],
                          ['extent_minimum', 'interval_depth_bottom']]

DEFAULT_VALUES = {'resource_type': 'Missing',
                  'resource_languages': 'eng',
                  'metadata_language': 'eng',
                  'metadata_standardName': 'ISO-USGIN',
                  'metadata_standardVersion': '1.1.4'}

VALID_LANGUAGE_CODES = ['aar','abk','ace','ach','ada','ady','afa','afh','afr','ain','aka','akk','ale','alg','alt','amh','ang','anp',
                       'apa','ara','arc','arg','arn','arp','art','arw','asm','ast','ath','aus','ava','ave','awa','aym','aze','bad',
                       'bai','bak','bal','bam','ban','bas','bat','bej','bel','bem','ben','ber','bho','bih','bik','bin','bis','bla',
                       'bnt','bos','bra','bre','btk','bua','bug','bul','byn','cad','cai','car','cat','cau','ceb','cel','cha','chb',
                       'che','chg','chk','chm','chn','cho','chp','chr','chu','chv','chy','cmc','cop','cor','cos','cpe','cpf','cpp',
                       'cre','crh','crp','csb','cus','dak','dan','dar','day','del','den','dgr','din','div','doi','dra','dsb','dua',
                       'dum','dyu','dzo','efi','egy','eka','elx','eng','enm','epo','est','ewe','ewo','fan','fao','fat','fij','fil',
                       'fin','fiu','fon','frm','fro','frr','frs','fry','ful','fur','gaa','gay','gba','gem','gez','gil','gla','gle',
                       'glg','glv','gmh','goh','gon','gor','got','grb','grc','grn','gsw','guj','gwi','hai','hat','hau','haw','heb',
                       'her','hil','him','hin','hit','hmn','hmo','hrv','hsb','hun','hup','iba','ibo','ido','iii','ijo','iku','ile',
                       'ilo','ina','inc','ind','ine','inh','ipk','ira','iro','ita','jav','jbo','jpn','jpr','jrb','kaa','kab','kac',
                       'kal','kam','kan','kar','kas','kau','kaw','kaz','kbd','kha','khi','khm','kho','kik','kin','kir','kmb','kok',
                       'kom','kon','kor','kos','kpe','krc','krl','kro','kru','kua','kum','kur','kut','lad','lah','lam','lao','lat',
                       'lav','lez','lim','lin','lit','lol','loz','ltz','lua','lub','lug','lui','lun','luo','lus','mad','mag','mah',
                       'mai','mak','mal','man','map','mar','mas','mdf','mdr','men','mga','mic','min','mis','mkh','mlg','mlt','mnc',
                       'mni','mno','moh','mon','mos','mul','mun','mus','mwl','mwr','myn','myv','nah','nai','nap','nau','nav','nbl',
                       'nde','ndo','nds','nep','new','nia','nic','niu','nno','nob','nog','non','nor','nqo','nso','nub','nwc','nya',
                       'nym','nyn','nyo','nzi','oci','oji','ori','orm','osa','oss','ota','oto','paa','pag','pal','pam','pan','pap',
                       'pau','peo','phi','phn','pli','pol','pon','por','pra','pro','pus','que','raj','rap','rar','roa','roh','rom',
                       'run','rup','rus','sad','sag','sah','sai','sal','sam','san','sas','sat','scn','sco','sel','sem','sga','sgn',
                       'shn','sid','sin','sio','sit','sla','slv','sma','sme','smi','smj','smn','smo','sms','sna','snd','snk','sog',
                       'som','son','sot','spa','srd','srn','srp','srr','ssa','ssw','suk','sun','sus','sux','swa','swe','syc','syr',
                       'tah','tai','tam','tat','tel','tem','ter','tet','tgk','tgl','tha','tig','tir','tiv','tkl','tlh','tli','tmh',
                       'tog','ton','tpi','tsi','tsn','tso','tuk','tum','tup','tur','tut','tvl','twi','tyv','udm','uga','uig','ukr',
                       'umb','und','urd','uzb','vai','ven','vie','vol','vot','wak','wal','war','was','wen','wln','wol','xal','xho',
                       'yao','yap','yid','yor','ypk','zap','zbl','zen','zha','znd','zul','zun','zxx','zza']

VALID_LENGTH_UNITS = ['m', 'ft']

COMMON_LANGUAGE_MISTAKES = {'english': 'eng'}

COMMON_LENGTH_MISTAKES = {'feet': 'ft',
                       'meter': 'm',
                       'meters': 'm',
                       'metres': 'm',
                       '': 'ft'}

COMMON_DATE_INPUT_FORMATS = ['%m/%d/%Y',
               '%m/%d/%YT%H:%M',
               '%b. %d %Y',
               '%b. %d, %Y',                   
               '%b %d %Y',
               '%b %d, %Y',
               '%B %d %Y',
               '%B %d, %Y',
               '%m-%d-%Y',
               '%m-%d-%YT%H:%M',
               '%m-%d-%Y %H:%M',
               '%m/%d/%Y %H:%M',
               '%Y-%m-%dT%H:%M',
               '%m/%Y',
               '%b. %Y',
               '%b %Y',
               '%B %Y']