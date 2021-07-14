import psycopg2
import csv
import pandas as pd
import numpy as np

def map_MC(s):
    if s in MC:
        return 'MC'
    elif s in MC1:
        return 'MC1'
    elif s in MC2:
        return 'MC2'
    elif s in MC3:
        return 'MC3'
    elif s in NP:
        return 'NP'

MC=['pb.abohar',
               'pb.amritsar',
               'pb.batala',
               'pb.bathinda',
               'pb.hoshiarpur',
               'pb.jalandhar',
               'pb.kapurthala',
               'pb.ludhiana',
               'pb.moga',
               'pb.mohali',
               'pb.pathankot',
               'pb.patiala',
               'pb.phagwara']

MC1 = ['pb.anandpursahib',
               'pb.barnala',
               'pb.derabassi',
               'pb.faridkot',
               'pb.fazilka',
               'pb.ferozepur',
               'pb.gurdaspur',
               'pb.jagraon',
               'pb.khanna',
               'pb.kharar',
               'pb.kotkapura',
               'pb.lalru',
               'pb.malerkotla',
               'pb.malout',
               'pb.mandigobindgarh',
               'pb.mansa',
               'pb.muktsar',
               'pb.nabha',
               'pb.nakodar',
               'pb.nangal',
               'pb.nawanshahr',
               'pb.rajpura',
               'pb.samana',
               'pb.sangrur',
               'pb.sunam',
               'pb.zirakpur']

MC2 = ['pb.adampur',
               	'pb.ahmedgarh',
               	'pb.baghapurana',
               	'pb.banga',
               	'pb.bhawanigarh',
               	'pb.bhogpur',
               	'pb.bhuchomandi',
               	'pb.budhlada',
               	'pb.dasuya',
               	'pb.dharamkot',
               	'pb.dhariwal',
               	'pb.dhuri',
               	'pb.dinanagar',
               	'pb.doraha',
               	'pb.garhshankar',
               	'pb.gidderbaha',
               	'pb.goniana',
               	'pb.goraya',
               	'pb.guruharsahai',
               	'pb.jaitu',
               	'pb.jalalabad',
               	'pb.jandialaguru',
               	'pb.kartarpur',
               	'pb.kurali',
               	'pb.lehragaga',
               	'pb.maur',
               	'pb.morinda',
               	'pb.mukerian',
               	'pb.mullanpur',
               	'pb.nayagaon',
               	'pb.nurmahal',
               	'pb.patran',
               	'pb.patti',
               	'pb.phillaur',
               	'pb.raikot',
               	'pb.raman',
               	'pb.rampuraphul',
               	'pb.ropar',
               	'pb.sahnewal',
               	'pb.samrala',
               	'pb.sirhind',
               	'pb.sujanpur',
               	'pb.sultanpurlodhi',
               	'pb.talwandibhai',
               	'pb.tarntaran',
               	'pb.urmartanda',
               	'pb.zira']

MC3 = ['pb.alawalpur',
               	'pb.amloh',
               	'pb.balachaur',
               	'pb.banur',
               	'pb.bareta',
               	'pb.bassipathana',
               	'pb.bhadaur',
               	'pb.derababananak',
               	'pb.dhanaula',
               	'pb.fatehgarhchurian',
               	'pb.garhdiwala',
               	'pb.hariana',
               	'pb.kotfatta',
               	'pb.longowal',
               	'pb.machhiwara',
               	'pb.majitha',
               	'pb.payal',
               	'pb.quadian',
               	'pb.rahon',
               	'pb.ramdass',
               	'pb.sanaur',
               	'pb.sangatmandi',
               	'pb.shamchurasi',
               	'pb.srihargobindpur',
               	'pb.tapa']

NP = ['pb.ajnala',
               	'pb.amargarh',
               	'pb.arniwala',
               	'pb.badhnikalan',
               	'pb.balianwali',
               	'pb.bariwala',
               	'pb.begowal',
               	'pb.bhadson',
               	'pb.bhagtabhai',
               	'pb.bhairoopa',
               	'pb.bhikhi',
               	'pb.bhikhiwind',
               	'pb.bhulath',
               	'pb.bilga',
               	'pb.boha',
               	'pb.chamkaursahib',
               	'pb.chaunke',
               	'pb.cheema',
               	'pb.dhilwan',
               	'pb.dirba',
               	'pb.fatehgarhpanjtoor',
               	'pb.ghagga',
               	'pb.ghanaur',
               	'pb.handiaya',
               	'pb.joga',
               	'pb.khamano',
               	'pb.khanauri',
               	'pb.khemkaran',
               	'pb.kiratpur',
               	'pb.kothaguru',
               	'pb.kotissekhan',
               	'pb.kotshamir',
               	'pb.lehramohabbat',
               	'pb.lohiankhas',
               	'pb.mahilpur',
               	'pb.makhu',
               	'pb.mallanwala',
               	'pb.maloud',
               	'pb.maluka',
               	'pb.mamdot',
               	'pb.mandikalan',
               	'pb.mehatpur',
               	'pb.mehraj',
               	'pb.moonak',
               	'pb.mudki',
               	'pb.nadala',
               	'pb.narotjaimalsingh',
               	'pb.nathana',
               	'pb.nihalsinghwala',
               	'pb.rajasansi',
               	'pb.rampura',
               	'pb.rayya',
               	'pb.sardulgarh',
               	'pb.shahkot',
               	'pb.talwandisabo',
               	'pb.talwara']

def map_ownershipsubtype(s):
    if s == 'Institutional':
        return 'Institutional'
    elif s == 'Individual':
        return 'Individual'
    elif s == 'Individual.Singleowner':
        return 'Single Owner'
    elif s == 'Institutionalgovernment.Stategovernment':
        return 'State Government'
    elif s == 'Institutionalgovernment.Ulbgovernment':
        return 'Ulb Government'
    elif s == 'Institutionalgovernment.Centralgovernment':
        return 'Central Government'
    elif s == 'Institutionalprivate.Othersgovernmentinstituition':
        return 'Other Government Instituition'
    elif s == 'Individual.Multipleowners':
        return 'Multiple Owners'
    elif s == 'Institutionalprivate.Privatetrust':
        return 'Private Trust'
    elif s == 'Institutionalprivate.Privatecompany':
        return 'Private Company'
    elif s == 'Institutionalprivate.Othersprivateinstituition':
        return 'Other Private Instituition'
    elif s == 'Institutionalprivate.Ngo':
        return 'Ngo'
    elif s == 'Institutionalprivate.Privateboard':
        return 'Private Board'
    
def map_ownershiptype(s):
    if s in Institutional:
        return 'Institutional'
    elif s in InstitutionalPrivate:
        return 'Institutional Private'
    elif s in InstitutionalGovernment:
        return 'Institutional Government'
    elif s in Individual:
        return 'Individual'

Institutional = ['Institutional']

InstitutionalPrivate = ['Other Private Instituition','Private Company','Private Board', 'Private Trust','Ngo']

InstitutionalGovernment = ['Other Government Instituition','State Government','Central Government','Ulb Government',]

Individual = ['Individual','Multiple Owners','Single Owner']

def map_ownershipsubtype(s):
    if s == 'Institutional':
        return 'Institutional'
    elif s == 'Individual':
        return 'Individual'
    elif s == 'Individual.Singleowner':
        return 'Single Owner'
    elif s == 'Institutionalgovernment.Stategovernment':
        return 'State Government'
    elif s == 'Institutionalgovernment.Ulbgovernment':
        return 'Ulb Government'
    elif s == 'Institutionalgovernment.Centralgovernment':
        return 'Central Government'
    elif s == 'Institutionalprivate.Othersgovernmentinstituition':
        return 'Other Government Instituition'
    elif s == 'Individual.Multipleowners':
        return 'Multiple Owners'
    elif s == 'Institutionalprivate.Privatetrust':
        return 'Private Trust'
    elif s == 'Institutionalprivate.Privatecompany':
        return 'Private Company'
    elif s == 'Institutionalprivate.Othersprivateinstituition':
        return 'Other Private Instituition'
    elif s == 'Institutionalprivate.Ngo':
        return 'Ngo'
    elif s == 'Institutionalprivate.Privateboard':
        return 'Private Board'
    
def map_ownershiptype(s):
    if s in Institutional:
        return 'Institutional'
    elif s in InstitutionalPrivate:
        return 'Institutional Private'
    elif s in InstitutionalGovernment:
        return 'Institutional Government'
    elif s in Individual:
        return 'Individual'
    
Institutional = ['Institutional']

InstitutionalPrivate = ['Other Private Instituition','Private Company','Private Board', 'Private Trust','Ngo']

InstitutionalGovernment = ['Other Government Instituition','State Government','Central Government','Ulb Government',]

Individual = ['Individual','Multiple Owners','Single Owner']

def map_status(s):
    if s == 'Pendingpayment':
        return 'Pending Payment'
    elif s == 'Pendingapproval':
        return 'Pending Approval' 
    elif s == 'Fieldinspection':
        return 'Field Inspection'
    elif s == 'Citizenactionrequired':
        return 'Citizen Action Required'
    elif s == 'Approved':
        return 'Approved'
    elif s == 'Expired':
        return 'Expired'
    elif s == 'Initiated':
        return 'Initiated'
    elif s == 'Cancelled':
        return 'Cancelled'
    elif s == 'Applied':
        return 'Applied'
    elif s == 'Rejected':
        return 'Rejected'
    elif s == 'Documentverify':
        return 'Document Verify'
    elif s == 'Citizenactionrequired-Dv':
        return 'Citizen Action Required - Dv'
    
def map_usagetype(s):
    if s == 'Group_A_Residential':
        return 'Group A Residential'
    elif s == 'Group_B_Educational':
        return 'Group B Educational' 
    elif s == 'Group_C_Institutional':
        return 'Group C Institutional'
    elif s == 'Group_D_Assembly':
        return 'Group D Assembly'
    elif s == 'Group_E_Business':
        return 'Group E Business'
    elif s == 'Group_F_Mercantile':
        return 'Group F Mercantile'
    elif s == 'Group_G_Industrial':
        return 'Group G Industrial'
    elif s == 'Group_H_Storage':
        return 'Group H Storage'
    elif s == 'Group_J_Hazardous':
        return 'Group J Hazardous'

def map_usagesubtype(s):
    if s == 'Subdivisiona-1':
        return 'Subdivision a-1'
    elif s == 'Subdivisiona-2':
        return ''
    elif s == 'Subdivisiona-3':
        return '' 
    elif s == 'Subdivisiona-4':
        return '' 
    elif s == 'Subdivisiona-5':
        return '' 
    elif s == 'Subdivisiona-6':
        return ''
    elif s == 'Subdivisionb-1':
        return '' 
    elif s == 'Subdivisionb-2':
        return '' 
    elif s == 'Subdivisionc-1':
        return '' 
    elif s == 'Subdivisionc-2':
        return '' 
    elif s == 'Subdivisionc-3':
        return '' 
    elif s == 'Subdivisiond-1':
        return '' 
    elif s == 'Subdivisiond-2':
        return '' 
    elif s == 'Subdivisiond-3':
        return '' 
    elif s == 'Subdivisiond-4':
        return '' 
    elif s == 'Subdivisiond-5':
        return '' 
    elif s == 'Subdivisiond-6':
        return '' 
    elif s == 'Subdivisiond-7':
        return ''
    elif s == 'Subdivisione-1':
        return '' 
    elif s == 'Subdivisione-2':
        return '' 
    elif s == 'Subdivisione-3':
        return '' 
    elif s == 'Subdivisione-4':
        return '' 
    elif s == 'Subdivisione-5':
        return ''
    elif s == 'Subdivisionf-1':
        return '' 
    elif s == 'Subdivisionf-2':
        return '' 
    elif s == 'Subdivisionf-3':
        return '' 
    elif s == 'Subdivisiong-1':
        return '' 
    elif s == 'Subdivisiong-2':
        return '' 
    elif s == 'Subdivisiong-3':
        return '' 
    elif s == 'Group_H_Storage':
        return 'Group H Storage'
    elif s == 'Group_J_Hazardous':
        return 'Group J Hazardous'
    
def map_gender(s):
    if s == 1.0:
        return 'Female'
    elif s == 2.0:
        return 'Male' 
    elif s == 3.0:
        return 'Transgender'


def connect():
    try:
        conn = psycopg2.connect(database="{{REPLACE-WITH-DATABASE}}", user="{{REPLACE-WITH-USERNAME}}",
                            password="{{REPLACE-WITH-PASSWORD}}", host="{{REPLACE-WITH-HOST}}")
        print("Connection established!")
        
    except Exception as exception:
        print("Exception occurred while connecting to the database")
        print(exception)
    
    query = pd.read_sql_query("SELECT fn.tenantid, fnd.applicationNumber AS \"Application Number\",fn.firenocnumber AS \"Fire NOC Number\", to_timestamp(CAST(fnd.applicationDate AS bigint)/1000)::date AS \"Application Date\", INITCAP(fnd.channel) AS \"Application Created By?\", INITCAP(fnd.status) AS \"Application Status\", fnd.financialYear AS \"Financial Year\", INITCAP(fnd.firenoctype) AS \"Fire NOC Type\",INITCAP( bld.usagetype) AS \"Usage Type\", INITCAP(SUBSTRING(fn.tenantid, 4)) AS \"City\", INITCAP(own.ownertype) AS \"Ownership Type\", usr.gender AS \"Owner Gender\", ep.totaldue As \"Total Amount Due\", ep.totalamountpaid as \"Total Amount Paid\", INITCAP(ep.paymentmode) AS \"Payment Mode\",to_timestamp(CAST(ep.createdtime AS bigint)/1000)::date AS \"Payment Date\" FROM eg_fn_firenoc fn INNER JOIN eg_fn_firenocdetail fnd ON fn.uuid = fnd.firenocuuid INNER JOIN eg_fn_buidlings bld ON fnd.uuid = bld.firenocdetailsuuid INNER JOIN eg_fn_address adr ON fnd.uuid = adr.firenocdetailsuuid INNER JOIN eg_fn_owner own  ON fnd.uuid = own.firenocdetailsuuid LEFT OUTER JOIN eg_user usr ON own.useruuid = usr.uuid LEFT OUTER JOIN egcl_bill eb ON  fnd.applicationNumber=eb.consumercode LEFT OUTER JOIN egcl_paymentdetail epd ON eb.id=epd.billid LEFT OUTER JOIN egcl_payment ep ON ep.id=epd.paymentid WHERE fn.tenantid != 'pb.testing'", conn)
    genderquery = pd.read_sql_query("SELECT fnd.applicationnumber AS \"Application Number\",usr.gender AS \"Application Created By Gender\" FROM eg_fn_firenoc fn INNER JOIN eg_fn_firenocdetail fnd ON fn.uuid = fnd.firenocuuid LEFT OUTER JOIN eg_user usr ON fn.createdby = usr.uuid WHERE fn.tenantid != 'pb.testing'", conn)
    provquery = pd.read_sql_query("SELECT fnd.applicationNumber AS \"Application Number\", fn.firenocnumber AS \"Fire NOC Number\", INITCAP( bld.usagetype) AS \"Usage Type\", INITCAP(own.ownertype) AS \"Ownership Type\" FROM eg_fn_firenoc fn INNER JOIN eg_fn_firenocdetail fnd ON fn.uuid = fnd.firenocuuid INNER JOIN eg_fn_owner own  ON fnd.uuid = own.firenocdetailsuuid INNER JOIN eg_fn_buidlings bld ON fnd.uuid = bld.firenocdetailsuuid WHERE fn.tenantid != 'pb.testing' AND fnd.firenoctype = 'PROVISIONAL'", conn)

   
    data = pd.DataFrame(query)
    gender = pd.DataFrame(genderquery)
    prov = pd.DataFrame(provquery)

    
    data['ULB Type'] = data['tenantid'].map(map_MC)
    data = data.drop(columns=['tenantid'])

    data.rename(columns = {'Ownership Type':'Ownership Subtype'},inplace = 'True')
    prov.rename(columns = {'Ownership Type':'Ownership Subtype'},inplace = 'True')
    
    data['Ownership Subtype'] = data['Ownership Subtype'].map(map_ownershipsubtype)
    data['Ownership Type'] = data['Ownership Subtype'].map(map_ownershiptype)
    prov['Ownership Subtype'] = prov['Ownership Subtype'].map(map_ownershipsubtype)
    prov['Ownership Type'] = prov['Ownership Subtype'].map(map_ownershiptype)
    
    data['Application Status'] = data['Application Status'].map(map_status)         

    data = data.rename(columns={"Usage Type": "usage_type"})
    prov = prov.rename(columns={"Usage Type": "usage_type"})

    data[['usage_type','Usage Subtype']] = pd.DataFrame(data.usage_type.str.split('.').tolist(),columns = ['usage_type','Trade Subtype'])
    prov[['usage_type','Usage Subtype']] = pd.DataFrame(prov.usage_type.str.split('.').tolist(),columns = ['usage_type','Trade Subtype'])

    data = data.rename(columns={"usage_type":"Usage Type"})
    prov = prov.rename(columns={"usage_type":"Usage Type"})

    data['Usage Type'] = data['Usage Type'].map(map_usagetype)         
    data['Usage Subtype'] = data['Usage Subtype'].map(map_usagesubtype)
    prov['Usage Type'] = prov['Usage Type'].map(map_usagetype)          
    prov['Usage Subtype'] = prov['Usage Subtype'].map(map_usagesubtype) 

    data = data.rename(columns={"Application Date": "Application_Date","Payment Date":"Payment_Date"})
    data['Application_Date'] = pd.to_datetime(data.Application_Date, format='%Y-%m-%d')
    data['Payment_Date'] = pd.to_datetime(data.Payment_Date, format='%Y-%m-%d')
    data['Application_Date'] = data['Application_Date'].dt.strftime("%d-%m-%y")
    data['Payment_Date'] = data['Payment_Date'].dt.strftime("%d-%m-%y")
    
    data = pd.merge(data, gender, how="left", left_on=["Application Number"],right_on = ["Application Number"])
    data['Owner Gender'] = data['Owner Gender'].map(map_gender)             
    data["Application Created By Gender"] = data["Application Created By Gender"].map(map_usagetype)         
    data = data.rename(columns={"Application_Date":"Application Date" ,"Commencement_Date":"Commencement Date","Payment_Date":"Payment Date"})
    
    data = data.rename(columns={"Ownership Type":"ownershiptype","Ownership Subtype":"ownershipsubtype","Usage Type":"usagetype","Usage Subtype":"usagesubtype"})
    prov = prov.rename(columns={"Ownership Type":"ownershiptype","Ownership Subtype":"ownershipsubtype","Usage Type":"usagetype","Usage Subtype":"usagesubtype"})
    result = pd.merge(data, prov, how="left", on=["Fire NOC Number"])
    result = result.drop_duplicates(subset = ["Fire NOC Number"])

    result['Usage Type Modified?'] = (result.usagetype_x!=result.usagetype_y)
    result['Usage Subtype Modified?'] = (result.usagesubtype_x!=result.usagesubtype_y)
    result['Ownership Type Modified?'] = (result.ownershiptype_x!=result.ownershiptype_y)
    result['Ownership Subtype Modified?'] = (result.ownershipsubtype_x!=result.ownershipsubtype_y)

    result['Data modified during new NOC creation?'] = result['Usage Type Modified?'] | result['Usage Subtype Modified?'] | result['Ownership Type Modified?'] | result['Ownership Subtype Modified?']
    columns_to_retain= ['Data modified during new NOC creation?','Fire NOC Number']
    result = result[columns_to_retain]
    result.loc[result['Fire NOC Number'].isnull(), 'Data modified during new NOC creation?'] = 'Not There'
    data = pd.merge(data,result, how="inner", on=["Fire NOC Number"])
    data['Data modified during new NOC creation?'] = data['Data modified during new NOC creation?'].map({True:'Yes',False:'No'}) 
    data = data.rename(columns={"ownershiptype":"Ownership Type","ownershipsubtype":"Ownership Subtype","usagetype":"Usage Type","usagesubtype":"Usage Subtype"})
    data.loc[data['Fire NOC Type'] == 'Provisional', 'Data modified during new NOC creation?'] = ''  
    data.loc[data['Data modified during new NOC creation?'] == 'Not There', 'Data modified during new NOC creation?'] = ''  

    data.fillna("", inplace=True)
     
    data.to_csv('/tmp/FNDatamart.csv')

    print("Datamart exported. Please copy it using kubectl cp command to your required location.")
    
if __name__ == '__main__':
    connect()
