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
    /*
    ConfirmDialog('Confirmation', 'Are you sure to power off the device?',
        function() {
            
            //document.location.href = '/v1/poweroff';
            
        });
    */
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

function ConfirmDialog(title, message, yesCallback) {
    $('<div></div>').appendTo('body')
        .html('<div><h6>' + message + '</h6></div>')
        .dialog({
            modal: true,
            title: title,
            zIndex: 10000,
            autoOpen: true,
            width: 'auto',
            resizable: false,
            buttons: {
                Yes: function() {
                    yesCallback();
                },
                No: function() {
                    $(this).dialog("close");
                }
            },
            close: function(event, ui) {
                $(this).remove();
            }
        });
}