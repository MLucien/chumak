"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
import zmq
import time
context = zmq.Context()

print('Connection to hello world server')
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

for request in range(100):
    message = socket.send("oi")
    print("Received reply %s [ %s ]" % (request, message))
    time.sleep(1)
