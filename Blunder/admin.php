<!DOCTYPE html> 
<html> 
<head> 
<title>Bludit</title> 
<meta charset="UTF-8"> 
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> 
<meta name="robots" content="noindex,nofollow"> 

  

<!-- Favicon --> 
<link rel="shortcut icon" type="image/x-icon" href="/bl-kernel/img/favicon.png?version=3.9.2"> 

  

<!-- CSS --> 
<link rel="stylesheet" type="text/css" href="http://10.129.83.108/bl-kernel/css/bootstrap.min.css?version=3.9.2"> 
<link rel="stylesheet" type="text/css" href="http://10.129.83.108/bl-kernel/admin/themes/booty/css/bludit.css?version=3.9.2"> 
<link rel="stylesheet" type="text/css" href="http://10.129.83.108/bl-kernel/admin/themes/booty/css/bludit.bootstrap.css?version=3.9.2"> 

  

<!-- Javascript --> 
<script src="http://10.129.83.108/bl-kernel/js/jquery.min.js?version=3.9.2"></script> 
<script src="http://10.129.83.108/bl-kernel/js/bootstrap.bundle.min.js?version=3.9.2"></script> 

<!-- Plugins --> 

</head> 
<body class="login"> 

<!-- Plugins --> 

<!-- Alert --> 

<script charset="utf-8"> 
function showAlert(text) { 
console.log("[INFO] Function showAlert() called."); 
$("#alert").html(text); 
$("#alert").slideDown().delay(3000).slideUp(); 
} 
$(window).click(function() { 
$("#alert").hide(); 
}); 

</script> 

  
<div id="alert" class="alert alert-success"></div> 

<div class="container"> 

<div class="row justify-content-md-center pt-5"> 

<div class="col-md-4 pt-5"> 

<h1 class="text-center mb-5 mt-5 font-weight-normal" style="color: #555;">BLUDIT</h1><form    method="post" action=""  autocomplete="off"><input type="hidden" id="jstokenCSRF" name="tokenCSRF" value="1f85fb0f6e7fd36827f66be0e8c780de46b8976e"> 

<div class="form-group"> 

<input type="text" value="" class="form-control form-control-lg" id="jsusername" name="username" placeholder="Username" autofocus> 

</div> 

<div class="form-group"> 

<input type="password" class="form-control form-control-lg" id="jspassword" name="password" placeholder="Password"> 

</div> 

<div class="form-check"> 

<input class="form-check-input" type="checkbox" value="true" id="jsremember" name="remember"> 

<label class="form-check-label" for="jsremember">Remember me</label> 

</div> 

  

<div class="form-group mt-4"> 

<button type="submit" class="btn btn-primary btn-lg mr-2 w-100" name="save">Login</button> 

</div> 

</form> </div> 

</div> 

</div> 

  

<!-- Plugins --> 

  

</body> 

</html> 

 

 