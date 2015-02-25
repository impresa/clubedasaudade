var TugaTweet = TugaTweet || (function(){

    function TugaTweetImpl() {
        _init();
    }

    function _init() {
        $('#search').submit(function(event) {

            $.ajax()

            event.preventDefault();
        });
    }

    return TugaTweetImpl()

})();