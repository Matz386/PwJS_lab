function checkForm()
{
    var error=false;
    var errorText="";
    var contactNameSurname=document.getElementById("contactNameSurname");
    var contactEmail=document.getElementById("contactEmail");

    if(contactNameSurname.value=="")
    {
        document.getElementById(‘errorNameSurname’).className=’alert alertdanger’;
        error=true;
    }

    if(contactEmail.value=="")
    {
        document.getElementById(‘errorEmail’).className=’alert alertdanger’;
        error=true;
    }
    else
    {
        var email=contactEmail.value;
        var regex =  /^[a-zA-Z0-9._-]+@([a-zA-Z0-9.-]+\.)+[a-zA-Z0-9.-]{2,4}$/; 
        if(regex.test(email)==false)
        {
            errorText+="Błędny format adresu email\n";
            error=true;
        }
    }
        
    if(!error)
        return true;
    else
    {
        return false;
    }
}