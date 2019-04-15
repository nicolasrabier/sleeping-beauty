$('#startstopmonitoring').click(function() {
    document.location.href = '';
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
