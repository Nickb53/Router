# Final Skeleton
#
# Hints/Reminders from Lab 4:
# 
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the 
# switch should send the packets out:
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    # This is where you'll put your code. The following modifications have 
    # been made from Lab 4:
    #   - port_on_switch represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)
    

    #TODO write table rules for floor 1 switch 1
    
	 # Incoming packets either go to core switch, host10, or host20
	 # IP packets must be sent to a specific port depending on dest port
	 # all other packets can be flooded
     if switch_id == 1:

    	 msg1 = of.ofp_flow_mod()
    	 msg1.idle_timeout = 30
    	 msg1.hard_timeout = 30
    	 msg1.match.dl_type = 0x0800
    	 msg1.match.nw_dst = ('10.0.1.10')
    	 msg1.actions.append(of.ofp_action_output(port = 1))
    	 self.connection.send(msg1)

    	 msg2 = of.ofp_flow_mod()
    	 msg2.idle_timeout = 30
    	 msg2.hard_timeout = 30
    	 msg2.match.dl_type = 0x0800
    	 msg2.match.nw_dst =('10.0.2.20')
    	 msg2.actions.append(of.ofp_action_output(port = 2))
    	 self.connection.send(msg2)
         
         msg3 = of.ofp_flow_mod()
         msg3.idle_timeout = 30
	 msg3.hard_timeout = 30
	 msg3.match.dl_type = 0x0800
         msg3.actions.append(of.ofp_action_output(port = 3))
	 self.connection.send(msg3)

	 msg4 = of.ofp_flow_mod()
	 msg4.idle_timeout = 30
	 msg4.hard_timeout = 30
	 msg4.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
	 self.connection.send(msg4)
	
    #TODO write table rules for floor 1 switch 2
     if(switch_id == 2):	 
    	 msg1 = of.ofp_flow_mod()
    	 msg1.idle_timeout = 30
    	 msg1.hard_timeout = 30
    	 msg1.match.dl_type = 0x0800
    	 msg1.match.nw_dst = ('10.0.3.30')
    	 msg1.actions.append(of.ofp_action_output(port = 1))
    	 self.connection.send(msg1)

    	 msg2 = of.ofp_flow_mod()
    	 msg2.idle_timeout = 30
    	 msg2.hard_timeout = 30
    	 msg2.match.dl_type = 0x0800
    	 msg2.match.nw_dst =('10.0.4.40')
    	 msg2.actions.append(of.ofp_action_output(port = 2))
    	 self.connection.send(msg2)
         
         msg3 = of.ofp_flow_mod()
         msg3.idle_timeout = 30
	 msg3.hard_timeout = 30
	 msg3.match.dl_type = 0x0800
         msg3.actions.append(of.ofp_action_output(port = 3))
	 self.connection.send(msg3)

	 msg4 = of.ofp_flow_mod()
	 msg4.idle_timeout = 30
	 msg4.hard_timeout = 30
	 msg4.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
	 self.connection.send(msg4)
    #TODO write table rules for floor 2 switch 1
     if(switch_id == 3):
	 
    	 msg1 = of.ofp_flow_mod()
    	 msg1.idle_timeout = 30
    	 msg1.hard_timeout = 30
    	 msg1.match.dl_type = 0x0800
    	 msg1.match.nw_dst = ('10.0.5.50')
    	 msg1.actions.append(of.ofp_action_output(port = 1))
    	 self.connection.send(msg1)

    	 msg2 = of.ofp_flow_mod()
    	 msg2.idle_timeout = 30
    	 msg2.hard_timeout = 30
    	 msg2.match.dl_type = 0x0800
    	 msg2.match.nw_dst =('10.0.6.60')
    	 msg2.actions.append(of.ofp_action_output(port = 2))
    	 self.connection.send(msg2)
         
         msg3 = of.ofp_flow_mod()
         msg3.idle_timeout = 30
	 msg3.hard_timeout = 30
	 msg3.match.dl_type = 0x0800
         msg3.actions.append(of.ofp_action_output(port = 3))
	 self.connection.send(msg3)

	 msg4 = of.ofp_flow_mod()
	 msg4.idle_timeout = 30
	 msg4.hard_timeout = 30
	 msg4.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
	 self.connection.send(msg4)
    #TODO write table rules for floow 2 switch 2
     if(switch_id == 4):
	 
    	 msg1 = of.ofp_flow_mod()
    	 msg1.idle_timeout = 30
    	 msg1.hard_timeout = 30
    	 msg1.match.dl_type = 0x0800
    	 msg1.match.nw_dst = ('10.0.7.70')
    	 msg1.actions.append(of.ofp_action_output(port = 1))
    	 self.connection.send(msg1)

    	 msg2 = of.ofp_flow_mod()
    	 msg2.idle_timeout = 30
    	 msg2.hard_timeout = 30
    	 msg2.match.dl_type = 0x0800
    	 msg2.match.nw_dst =('10.0.8.80')
    	 msg2.actions.append(of.ofp_action_output(port = 2))
    	 self.connection.send(msg2)
         
         msg3 = of.ofp_flow_mod()
         msg3.idle_timeout = 30
	 msg3.hard_timeout = 30
	 msg3.match.dl_type = 0x0800
         msg3.actions.append(of.ofp_action_output(port = 3))
	 self.connection.send(msg3)

	 msg4 = of.ofp_flow_mod()
	 msg4.idle_timeout = 30
	 msg4.hard_timeout = 30
	 msg4.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
	 self.connection.send(msg4)
    #TODO write table rules for core switch and data center switch
     if(switch_id == 5):
	 
	
	 msg = of.ofp_flow_mod()
	 msg.idle_timeout = 0
	 msg.hard_timeout = 0
	 msg.match.dl_type = 0x0800
	 msg.match.nw_dst = ('10.0.9.10')
	 msg.match.in_port = 5
	 msg.actions.append(of.ofp_action_output(port = 5))
	 self.connection.send(msg)
 

	 msg0 = of.ofp_flow_mod()
	 msg0.idle_timeout = 0
	 msg0.hard_timeout = 0
	 msg0.match.dl_type = 0x0800
	 msg0.match.nw_proto = 1
	 msg0.match.in_port = 5
	 msg0.actions.append(of.ofp_action_output(port = 5))
	 self.connection.send(msg0)
 
	 msg1 = of.ofp_flow_mod()
	 msg1.idle_timeout = 30
	 msg1.hard_timeout = 30
    	 msg1.match.dl_type = 0x0800
	 msg1.match.nw_dst = ('10.0.1.10')
	 msg1.actions.append(of.ofp_action_output(port = 1))
	 self.connection.send(msg1) 
    
	 msg2 = of.ofp_flow_mod()
	 msg2.idle_timeout = 30
	 msg2.hard_timeout = 30
    	 msg2.match.dl_type = 0x0800
	 msg2.match.nw_dst = ('10.0.2.20')
	 msg2.actions.append(of.ofp_action_output(port = 1))
	 self.connection.send(msg2) 

	#3 and 4
	 msg3 = of.ofp_flow_mod()
	 msg3.idle_timeout = 30
	 msg3.hard_timeout = 30
    	 msg3.match.dl_type = 0x0800
	 msg3.match.nw_dst = ('10.0.3.30')
	 msg3.actions.append(of.ofp_action_output(port = 2))
	 self.connection.send(msg3)

	 msg4 = of.ofp_flow_mod()
	 msg4.idle_timeout = 30
	 msg4.hard_timeout = 30
    	 msg4.match.dl_type = 0x0800
	 msg4.match.nw_dst = ('10.0.4.40')
	 msg4.actions.append(of.ofp_action_output(port = 2))
	 self.connection.send(msg4) 

	#5 and 6

	 msg5 = of.ofp_flow_mod()
	 msg5.idle_timeout = 30
	 msg5.hard_timeout = 30
    	 msg5.match.dl_type = 0x0800
	 msg5.match.nw_dst = ('10.0.5.50')
	 msg5.actions.append(of.ofp_action_output(port = 3))
	 self.connection.send(msg5) 

	 msg6 = of.ofp_flow_mod()
	 msg6.idle_timeout = 30
	 msg6.hard_timeout = 30
    	 msg6.match.dl_type = 0x0800
	 msg6.match.nw_dst = ('10.0.6.60')
	 msg6.actions.append(of.ofp_action_output(port = 3))
	 self.connection.send(msg6) 
	#7 and 8

	 msg7 = of.ofp_flow_mod()
	 msg7.idle_timeout = 30
	 msg7.hard_timeout = 30
    	 msg7.match.dl_type = 0x0800
	 msg7.match.nw_dst = ('10.0.7.70')
	 msg7.actions.append(of.ofp_action_output(port = 4))
	 self.connection.send(msg7) 
 
	 msg8 = of.ofp_flow_mod()
	 msg8.idle_timeout = 30
	 msg8.hard_timeout = 30
    	 msg8.match.dl_type = 0x0800
	 msg8.match.nw_dst = ('10.0.8.80')
	 msg8.actions.append(of.ofp_action_output(port = 4))
	 self.connection.send(msg8)

	 msgS = of.ofp_flow_mod()
	 msgS.idle_timeout = 30
	 msgS.hard_timout = 30
	 msgS.match.dl_type = 0x0800
	 msgS.match.nw_dst = ('10.0.9.10')
	 msgS.actions.append(of.ofp_action_output(port = 6))
	 self.connection.send(msgS)

	 msgU = of.ofp_flow_mod()
	 msgU.idle_timeout = 30
	 msgU.hard_timeout = 30
	 msgU.match.dl_type = 0x0800
	 msgU.match.nw_dst = ('10.0.9.99')
	 msgU.actions.append(of.ofp_action_output(port = 5))
	 self.connection.send(msgU)

	 msg9 = of.ofp_flow_mod()
	 msg9.idle_timeout = 30
	 msg9.hard_timeout = 30
	 msg9.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
	 self.connection.send(msg9)


     if(switch_id == 6):

	msg1 = of.ofp_flow_mod()
	msg1.idle_timeout = 30
	msg1.hard_timeout = 30
	msg1.match.dl_type = 0x0800
	msg1.match.nw_dst = ('10.0.9.10')
	msg1.actions.append(of.ofp_action_output(port = 1))
	self.connection.send(msg1)

	msg2 = of.ofp_flow_mod()
	msg2.idle_timeout = 30
	msg2.hard_timeout = 30
	msg2.match.dl_type = 0x0800
	msg2.actions.append(of.ofp_action_output(port = 3))
	self.connection.send(msg2)	

	msg3 = of.ofp_flow_mod()
	msg3.idle_timeout = 30
	msg3.hard_timeout = 30
	msg3.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
	self.connection.send(msg3)
	 
  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
