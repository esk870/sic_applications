import time 

from sic_framework.devices.common_naoqi.naoqi_autonomous import NaoBackgroundMovingRequest, NaoBasicAwarenessRequest,\
     NaoWakeUpRequest , NaoRestRequest

from sic_framework.devices.common_naoqi.naoqi_motion import NaoqiAnimationRequest, NaoqiIdlePostureRequest , \
    NaoqiBreathingRequest, NaoPostureRequest

from sic_framework.devices import Nao


#ATTENTION: Start Redit Server before running this code 

#Connect to Robot
nao = Nao("192.168.0.240") # CHANGE ID HERE


#Robot Postures for Interaction Task 
#Overview Animations: http://doc.aldebaran.com/2-4/naoqi/motion/alanimationplayer-advanced.html#animationplayer-list-behaviors-nao
#All Postures: "Crouch", "LyingBack", "LyingBelly", "Sit", "SitRelax", Stand", "StandInit", "StandZero", 
#Overview Bodyparts: http://doc.aldebaran.com/2-8/family/nao_technical/bodyparts_naov6.html#nao-chains


#Robot waves
nao.motion.request(NaoqiAnimationRequest("animations/Stand/Gestures/Hey_1"))

#Starting Positon of Robot 
nao.motion.request(NaoPostureRequest("Stand")) # Definition idle posture
nao.motion.request(NaoqiIdlePostureRequest("Body", True)) #After action robot goes back to idle posture (i.e., Keeps standing in our case)

#Robot looks like he is breathing
nao.motion.request(NaoqiBreathingRequest("Body", True))

#Robot looks at speaker
nao.autonomous.request(NaoBackgroundMovingRequest(True))
nao.autonomous.request(NaoBasicAwarenessRequest(True))

#Robot stands up/goes back to crouching (Alternative to pressing button on robot)
nao.autonomous.request(NaoWakeUpRequest())
nao.autonomous.request(NaoRestRequest())


nao.stop()

