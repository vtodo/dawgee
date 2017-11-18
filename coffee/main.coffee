beta = require('./beta.coffee')
class SocketClient
    constructor:->
        host = window.location.host
        ws = new WebSocket('ws://'+host+'/ws')
        ws.onopen = ()=>
            console.log "Connected"
        ws.onclose = ()=>
            console.log "Close"
        ws.onerror = ()=>
            console.log "Error"
        ws.onmessage = ()=>
            console.log "Received message"
        

client = new SocketClient()