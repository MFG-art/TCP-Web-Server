function ready(callback){
    // in case the document is already rendered
    if (document.readyState !== 'loading'){
		callback();
    }
    else {
		document.addEventListener('DOMContentLoaded', callback);
    }
}

ready(resizeLogic);

function resizeLogic() {
    var id;
    var parentEventReceived = false;

    window.addEventListener('message', listenToHost, false);

    function listenToHost(event) {
        try {
            var data = JSON.parse(event.data);

            if (data.handler !== 'd2l.iframe.client') {
                return;
            }

            id = data.id;

            parentEventReceived = true;
            doResize();
        } catch (e) {
            console.warn('iframe-client: not handling unexpected message posted by another window: ', event.data);
        }
    }

    function doResize() {
        var height;

        if ( parentEventReceived ) {
            window.scrollTo(0, 0);
        }

        height = getHeight();

        //When the page is within a frameset, must not post frame size fit messages
        if( !ContainsFrameset() ) {
            if ( parentEventReceived ) {
                document.body.style.overflowY = 'hidden';
            }
            window.top.postMessage( JSON.stringify( { handler: 'd2l.iframe.host', id: id, height: height } ), '*' );
            setTimeout( function() { doResize(); }, 500 );
        }
    }

    function ContainsFrameset() {
        try {
            if (parent.document.getElementsByTagName('frameset').length > 0) {
                //Page within a frameset
                return true;
            } else {
                //Page not within a frameset.
                return false;
            }
        } catch (e) {
            //Expected case: Classic page not within a frameset!
            //Could not access iframe on host due to normal browser security contraints 
            return false;
        }
    }

    function getHeight() {
        // This method is relatively expensive, but it seems to be the only one that reliably catches changes that shrink the content
        var maxBottomVal = 0;

		var items = document.body.getElementsByTagName("*");
		for (var i = 0, len = items.length; i < len; i++) {
			var elBottom = items[i].getBoundingClientRect().bottom;
            if (elBottom > maxBottomVal) {
                maxBottomVal = elBottom;
            }
		}

        return maxBottomVal + 1;
    }
	doResize();
}