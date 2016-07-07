val={ 'Email':[IS_NOT_EMPTY(),IS_EMAIL()] ,
      'EmailMass':[IS_NOT_EMPTY(),IS_EMAIL_MASS()]}

@auth.requires_login()
def __entries():
    rows=semester().select(Whitelist.ALL)
    array=[]
    for row in rows:
        entry={'UniqueId'    :row.UniqueId,
               'Email'       :row.Email}
        array.append(entry)
    return dict(entries=array)

@auth.requires_login()
def index():
    returnDict={}
    returnDict.update(__entries())
    return returnDict

@auth.requires_login()
def newEmail():
    returnDict={}

    inputs=TD(INPUT(_name='Email',_size="30",_placeholder=" Student Email", requires= val['Email'] )),\
           TD(INPUT(_type='submit',_label='Save'))
    form=FORM(inputs)

    if(form.process().accepted):
        #strip all whitespaces from begin and end
        for var in form.vars:
            var=var.strip().strip('\r')
        Whitelist.insert(Email=form.vars.Email)
        redirect(URL('index'))

    returnDict.update({'form':form})
    returnDict.update(__entries())

    return returnDict

@auth.requires_login()
def deleteEmail():
    UniqueId= request.vars['UniqueId']
    if semester(Whitelist.UniqueId==UniqueId).delete() :
        msg='Email deleted'
    else:
        msg='User delete failed'
    redirect(URL('index'))
    
@auth.requires_login()
def massEmail():
    returnDict={}

    inputs=TR(TD(TEXTAREA(_name='EmailMass',_requires=val['EmailMass'],_cols="60",_rows="30"))),\
           TR(TD(INPUT(_type='submit',_label='Save')))
    form=FORM(inputs)
    if form.process().accepted:
        Emails=form.vars.EmailMass.split('\n')
        for Email in Emails:
            #delete whitespaces from begin and end and returns
            Email=Email.strip('\r')
            Email=Email.strip()

            Whitelist.insert(Email=Email)

        redirect(URL('index'))

    returnDict.update({'form':form})
    return returnDict
