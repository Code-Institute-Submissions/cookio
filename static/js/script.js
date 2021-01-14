 $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();

    const modalOkBtn = document.getElementById('modal-ok-btn');

    $('.remove-btn').click((event) => {
        const modal = document.getElementById('confirmation-dialog');
        const instance = M.Modal.init(modal, { dismissible:false });
        instance.open();

        modalOkBtn.href = event.currentTarget.href;

        return false;
    });
  });