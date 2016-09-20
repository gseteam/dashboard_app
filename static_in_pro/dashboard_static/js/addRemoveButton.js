/**
 * Created by jaiswroh on 9/5/2016.
 */
$(document).ready(function() {

    $('#btn-add').click(function(){
        $('#select-from option:selected').each( function() {
                 if ($(this).text()!="Remove-Activity"){
                $('#select-to').append("<option>"+$(this).text()+"</option>");
                 //alert($(this).text());
            $(this).remove();}
        });
    });
    $('#btn-remove').click(function(){
        $('#select-to option:selected').each( function() {
           if ($(this).text()!="Add-activity"){
                $('#select-from').append("<option>"+$(this).text()+"</option>");
                 //alert($(this).text());
            $(this).remove();}
        });
    });

});
