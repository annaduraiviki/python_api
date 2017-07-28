import plivo

auth_id = 'MAMWYZODEYYJHMMGZMOT'
auth_token = 'ZDM4YzliOWY0NTQ4MWU2NzgzNzQ4ZWFhNDM2ZTM0'

p = plivo.RestAPI(auth_id, auth_token)

params = {'src': '+919626909678',
          'dst': '+919626909678',
#'ring_url': 'http://example.com/ring_url',
        'text' : u"Hello, how are you from pilvo?"
# 'answer_url': 'http://example.com/answer_url',
# 'hangup_url': 'http://example.com/hangup_url'
}

response = p.send_message(params)