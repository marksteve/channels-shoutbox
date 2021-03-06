var ws = new WebSocket('ws://' + location.host + '/shoutbox')
var messages = $('.messages')
var form = $('form')
var colorHash = new ColorHash()

function sendMessage(e) {
  e.preventDefault()
  var name = form.name.value
  if (!name) {
    return
  }
  var text = form.text.value
  ws.send(JSON.stringify({
    name: name,
    text: text,
  }))
  form.text.value = null
}

function recvMessage(e) {
  var data = JSON.parse(e.data)
  var message = $.create('li', {
    className: 'message border-bottom border-silver p2',
    title: data.sent_at,
    contents: [
      {tag: 'strong', textContent: data.name},
      {tag: 'span', textContent: ' ' + data.text},
    ]
  })
  message._.start(messages)
  onmount()
}

function setNameColor() {
  var name = $('strong', this)
  name._.style({color: colorHash.hex(name.textContent)})
}

form._.events({submit: sendMessage})
ws.onmessage = recvMessage
onmount('.message', setNameColor)
onmount()
