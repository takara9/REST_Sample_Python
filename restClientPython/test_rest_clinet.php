<?php
include "cfenv.php";
include "rest_if.php";

$vcap = new Cfenv();
$vcap->byInstName('pycalcxxu');

print "username = ".$vcap->user."\n";
print "password = ".$vcap->pass."\n";
print "REST Service URI = ".$vcap->uri."\n";

$param['username'] = $vcap->user;
$param['password'] = $vcap->pass;

$param['a'] = 391.345;
$param['b'] = 5.4452;

print "----------------------\n";
print "Input A = ".$param['a']."\n";
print "Input B = ".$param['b']."\n";

$post['json'] = json_encode($param);
$url = $vcap->uri;

$reply = curl_post($url,$post);
$result = json_decode($reply);

if (isset($result->{'error'})) {
   print "error = ".$result->{'error'}."\n";
} else {
  print "Result = ".$result->{'ans'}."\n";
}

?>


