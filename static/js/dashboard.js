$('#startstopmonitoring').click(function() {
    if($('#monitoringstatus').text() == 'STOPPED') {
        document.location.href = '/v1/startmonitoring';
    } else {
        document.location.href = '/v1/stopmonitoring';
    }
});
$('#turnvolumedown').click(function() {
    document.location.href = '';
});
$('#turnvolumeup').click(function() {
    document.location.href = '';
});
$('#poweroff').click(function() {
    $('#poweroff').toggle(false);
    $('#poweroffconfirm').toggle(true);
    $('#poweroffcancel').toggle(true);
});
$('#poweroffconfirm').click(function() {
    document.location.href = '/v1/poweroff';
});
$('#poweroffcancel').click(function() {
    $('#poweroff').toggle(true);
    $('#poweroffconfirm').toggle(false);
    $('#poweroffcancel').toggle(false);
});
$('#status').click(function() {
    document.location.href = '/v1/status';
});

$( document ).ready(function() {
    $('#messagebox').text("Your screen resolution is: " + window.screen.width * window.devicePixelRatio + "x" + window.screen.height * window.devicePixelRatio);
});

