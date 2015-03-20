$(document).ready(function(){

    $('#drag-option').change(function(){
        $('.drag-vel-fields').toggle(this.checked);
        $('.drag-den-fields').toggle(this.checked);
    })


    // Hide Unnecessary Velocity Drag Fields
    $(function(){
        $('.RO').hide();
        $('#vel-field').change(function(){
            if($('#vel-field').val() == 'RO'){
                $('.RO').show();
            } else {
                $('.RO').hide();
            }
        });
    })

    //Hide Unnecessary Density Drag Fields
    $(function(){
        $('.PL').hide();
        $('.DD').hide();

        $('#den-field').change(function(){
            if($('#den-field').val() == 'CD'){
                $('.CD').show();
            } else {
                $('.CD').hide();
            }

            if($('#den-field').val() == 'PL'){
                $('.PL').show();
            } else {
                $('.PL').hide();
            }

            if($('#den-field').val() == 'DD'){
                $('.DD').show();
            } else {
                $('.DD').hide();
            }
        })
    });

    //Hide Unnecessary Potential Fields
    $(function(){
        $('.PS').hide();
        $('#potential-field').change(function(){
            if($('#potential-field').val() == 'WF'){
                $('.WF').show();
            } else {
                $('.WF').hide();
            }

            if($('#potential-field').val() == 'PS'){
                $('.PS').show();
            } else {
                $('.PS').hide();
            }
        })
    });

});
