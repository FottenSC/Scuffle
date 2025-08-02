from enum import Enum, Flag


def enum_has_value(cls, value):
    return any(value == item.value for item in cls)
def name_from_enum(cls, value, replace_char = " ", format = False, slice = False, slice_index = 0):
    try:
        if enum_has_value(cls, value):
            result = cls(value).name
            result = result.replace("__", " > ")
            if slice:
                result = result.split("_")[slice_index]
            if format:
                result = result.capitalize()
            
            return f'{result.replace("_", replace_char)}'
        else:
            return value
    
    except:
        return value


class BoolFlag(Enum):
    False_ = 0x00
    True_ = 0x01

class Button(Enum):
    A = 0x01
    B = 0x02
    K = 0x04
    G = 0x08

    B_K = 0x06
    A_B = 0x03
    A_G = 0x09
    K_G = 0x0C

    A_B_K = 0x07


class PaddedButton(Enum):
    U = 0xAAAA
    RE = 0xAAAB

    A = 0x0001
    B = 0x0002
    K = 0x0004
    G = 0x0008

    A_B = 0x0300
    A_K = 0x0500
    B_K = 0x0600
    A_G = 0x0900
    B_G = 0x0a00
    K_G = 0x0C00
    
    A_B_K = 0x0700
    A_B_K_G = 0x0F00
    
    Forward = 0x1008
    Forward_ALT = 0x3008

    d = 0x9999

    b = 0x002e
    h = 0x001b
    #c =
    dd = 0x0054

    Back = 0x1002
    Back_ALT = 0x3004

    Right = 0x1004
    Right_ALT = 0x4004

    Left = 0x1006
    Left_ALT = 0x4008


class EffectPart(Enum):
    BASE = 0x0
    STOMACH = 0x01
    LOWER_CHEST = 0x02
    UPPER_CHEST = 0x03
    NECK = 0x04
    HEAD = 0x05
    RIGHT_COLLARBONE = 0x06
    RIGHT_SHOULDER = 0x07
    RIGHT_ARM = 0x08
    RIGHT_HAND = 0x09
    LEFT_COLLARBONE = 0x0a
    LEFT_SHOULDER = 0x0b
    LEFT_ARM = 0x0c
    LEFT_HAND = 0x0d
    WAIST = 0x0e
    RIGHT_THIGH = 0x0f
    RIGHT_KNEE = 0x10
    RIGHT_FOOT = 0x11
    RIGHT_TOE = 0x12
    LEFT_THIGH = 0x13
    LEFT_KNEE = 0x14
    LEFT_FOOT = 0x15
    LEFT_TOE = 0x16
    WEAPON_1 = 0x17
    WEAPON_2 = 0x18
    WEAPON_3 = 0x19
    WEAPON_4 = 0x1a
    WEAPON_5 = 0x1b
    WEAPON_6 = 0x1c
    WEAPON_7 = 0x1d
    WEAPON_8 = 0x1e
    WEAPON_9 = 0x1f
    WEAPON_SOCKET_1 = 0x8017
    WEAPON_SOCKET_2 = 0x8018
    WEAPON_SOCKET_3 = 0x8019
    WEAPON_SOCKET_4 = 0x801a
    WEAPON_SOCKET_5 = 0x801b
    WEAPON_SOCKET_6 = 0x801c
    WEAPON_SOCKET_7 = 0x801d
    WEAPON_SOCKET_8 = 0x801e
    WEAPON_SOCKET_9 = 0x801f
    RIGHT_THUMB_3 = 0x20
    RIGHT_THUMB_2 = 0x21
    RIGHT_THUMB_1 = 0x22
    RIGHT_INDEX_FINGER_3 = 0x23
    RIGHT_INDEX_FINGER_2 = 0x24
    RIGHT_INDEX_FINGER_1 = 0x25
    RIGHT_MIDDLE_FINGER_3 = 0x26
    RIGHT_MIDDLE_FINGER_2 = 0x27
    RIGHT_MIDDLE_FINGER_1 = 0x28
    RIGHT_RING_FINGER_3 = 0x29
    RIGHT_RING_FINGER_2 = 0x2a
    RIGHT_RING_FINGER_1 = 0x2b
    RIGHT_PINKY_FINGER_3 = 0x2c
    RIGHT_PINKY_FINGER_2 = 0x2d
    RIGHT_PINKY_FINGER_1 = 0x2e
    LEFT_THUMB_3 = 0x2f
    LEFT_THUMB_2 = 0x30
    LEFT_THUMB_1 = 0x31
    LEFT_INDEX_FINGER_3 = 0x32
    LEFT_INDEX_FINGER_2 = 0x33
    LEFT_INDEX_FINGER_1 = 0x34
    LEFT_MIDDLE_FINGER_3 = 0x35
    LEFT_MIDDLE_FINGER_2 = 0x36
    LEFT_MIDDLE_FINGER_1 = 0x37
    LEFT_RING_FINGER_3 = 0x38
    LEFT_RING_FINGER_2 = 0x39
    LEFT_RING_FINGER_1 = 0x3a
    LEFT_PINKY_FINGER_3 = 0x3b
    LEFT_PINKY_FINGER_2 = 0x3c
    LEFT_PINKY_FINGER_1 = 0x3d
    RIGHT_INNER_EYEBROW = 0x3e
    RIGHT_EYEBROW = 0x3f
    RIGHT_EYE = 0x40
    RIGHT_UPPER_EYELID = 0x41
    RIGHT_LOWER_EYELID = 0x42
    RIGHT_CHEEK = 0x43
    RIGHT_NOSTRIL = 0x44
    RIGHT_JAW = 0x45
    LEFT_INNER_EYEBROW = 0x46
    LEFT_EYEBROW = 0x47
    LEFT_EYE = 0x48
    LEFT_UPPER_EYELID = 0x49
    LEFT_LOWER_EYELID = 0x4a
    LEFT_CHEEK = 0x4b
    LEFT_NOSTRIL = 0x4c
    LEFT_JAW = 0x4d
    MIDDLE_UPPER_LIP = 0x4e
    RIGHT_UPPER_LIP = 0x4f
    LEFT_UPPER_LIP = 0x50
    JAW = 0x51
    RIGHT_LOWER_LIP = 0x52
    RIGHT_MOUTH_CORNER = 0x53
    LEFT_LOWER_LIP = 0x54
    LEFT_MOUTH_CORNER = 0x55
    TONGUE_1 = 0x56
    TONGUE_2 = 0x57
    OBJ_NUM = 0x58

class EffectTarget(Enum):
    Player = 0x01
    Opponent = 0x03
    Player__On_Ground = 0x05
    Opponent__On_Ground = 0x06

class TraceKind(Enum):
    AUTO = 0x00
    NORMAL = 0x01
    TUBE = 0x02
    LINE = 0x03
    THUNDER = 0x04
    WIND = 0x05
    FLAME = 0x06 #unblockable
    LIGHT = 0x07
    PFLAME = 0x08 
    PSMOKE = 0x09
    PBURN = 0x0a
    PLIGHT = 0x0b
    PFLAME_L = 0x0c
    PSMOKE_L = 0x0d
    PBURN_L = 0x0e
    PLIGHT_L = 0x0f
    PDUST = 0x10
    PDUST_L = 0x11
    PAURA = 0x12
    PAURA_L = 0x13
    SPARK = 0x14
    FIRE_S = 0x15
    PTHUNDER = 0x16 #break attack
    PWIND = 0x17
    LIGHTSABER = 0x18
    KICK = 0x19
    ULTIMATE_EDGE = 0x1a
    ULTIMATE_CALIBUR = 0x1b
    NORMAL_S = 0x1c #normal
    NORMAL_M = 0x1d #normal
    NORMAL_L = 0x1e #normal
    PTHUNDER_PINK = 0x1f #reversal edge start
    PTHUNDER_RED = 0x20 #reversal edge hold / during reversal edge
    SOUL_CHARGE_NORMAL_S = 0x21 #soul charge
    SOUL_CHARGE_NORMAL_M = 0x22 #soul charge
    SOUL_CHARGE_NORMAL_L = 0x23 #soul charge
    SOUL_CHARGE_PFLAME = 0x24 #soul charge unblockable
    SOUL_CHARGE_PTHUNDER = 0x25 #soul charge break attack
    SOUL_CHARGE_PTHUNDER_PINK = 0x26 #soul charge reversal edge start
    SOUL_CHARGE_PTHUNDER_RED = 0x27 #soul charge reversal edge hold / during reversal edge
    CE_1 = 0x28
    CE_2 = 0x29
    CE_3 = 0x2a
    SPECIAL_1 = 0x2b #SP_01
    SPECIAL_2 = 0x2c #SP_02
    SPECIAL_3 = 0x2d #SP_03
    SOUL_ATTACK = 0x2e #SP_04, always soul attack

class TracePart(Enum):
    NONE = 0xFFFF
    WEAPONS1 = 0X00 #ARMS1
    WEAPONS2 = 0x01 #ARMS2
    WEAPONS3 = 0x02 #ARMS3
    WEAPONS4 = 0x03 #ARMS4
    WEAPONS5 = 0x04 #ARMS5
    WEAPONS6 = 0x05 #ARMS6
    WEAPONS7 = 0x06 #ARMS7
    WEAPONS8 = 0x07 #ARMS8
    WEAPONS9 = 0x08 #ARMS9
    TAIL = 0x09
    CHEST = 0x0a #MUNE
    HEAD = 0x0b #ATAMA
    RIGHT_SHOULDER = 0x0c
    RIGHT_ARM = 0x0d
    RIGHT_HAND = 0x0e
    LEFT_SHOULDER = 0x0f
    LEFT_ARM = 0x10
    LEFT_HAND = 0x11
    WAIST = 0x12
    RIGHT_THIGH = 0x13
    RIGHT_LEG = 0x14
    RIGHT_FOOT = 0x15
    LEFT_THIGH = 0x16
    LEFT_LEG = 0x17
    LEFT_FOOT = 0x18
    RIGHT_EYE = 0x19
    LEFT_EYE = 0x1a
    AUO_1 = 0x1b
    AUO_2 = 0x1c
    AUO_3 = 0x1d
    AUO_4 = 0x1e
    AUO_5 = 0x1f
    AUO_6 = 0x20
    AUO_7 = 0x21
    AUO_8 = 0x22
    NM_THUMB = 0x23
    NM_INDEX_FINGER = 0x24
    NM_MIDDLE_FINGER = 0x25
    SPECIAL_1 = 0x26
    SPECIAL_2 = 0x27
    SPECIAL_3 = 0x28
    SPECIAL_4 = 0x29
    SPECIAL_5 = 0x2a
    SPECIAL_6 = 0x2b
    SPECIAL_7 = 0x2c
    SPECIAL_8 = 0x2d
    SPECIAL_9 = 0x2e
    





class InputType(Enum):
    Press = 0x06
    Hold = 0x05
    _Hold = 0x20  

    Direction_PRESS = 0x13AF
    Direction_HOLD= 0x13AE
    Direction_ALT = 0x0002
    No_SC_Press =0x8f #for when you're not in soul charge???


    OnContact = 0x0B #counter hit uses the same code signature but are about 3x as long so the counterhit part must be in there somewhere

    DoubleTap = 0x2C

    #PressDown = 0x13af /0x13ae ??
    #PressBack =  0x0002 /0x1002 ??
    #0x0120 #geralt, super?? + hold button

class ComboConditions(Flag):
    Counter_Hit = 0x01
    Prevent_Chain = 0x08
    Jail_on_Block = 0x20

class ReturnState(Enum):
    STANDING = 0xc8
    CROUCHING = 0xc9
    STANDING_GUARD = 0xca
    CROUCHING_GUARD = 0xcb
    GROUNDED_FACE_UP = 0xd0
    GROUNDED_FACE_DOWN = 0xd1
    BT_STANDING = 0xd2
    BT_CROUCHING = 0xd3
    CROUCHING__STANDING = 0xd4
    BT_CROUCHING__STANDING = 0xd5
    BT_GROUNDED_FACE_UP = 0xdc
    BT_GROUNDED_FACE_DOWN = 0xdd


class SpecialState(Enum):
    TECH_CROUCH = 0x02
    GROUNDED = 0x03
    TECH_JUMP = 0x04
    GUARD_IMPACT = 0x0a
    ATTACK_HIT = 0x1b
    ATTACK_MISS = 0x1c
    WALL_HIT = 0x1f
    INVISIBLE = 0x23
    RING_OUT = 0x28
    TECH_COUNTER = 0x2b
    BLOCK = 0x2e
    CROUCHING_ATTACK = 0x68
    WHILE_RISING_ATTACK = 0x69
    MULTI_PRESS_ATTACK = 0x6a
    _8WAYRUN_ATTACK = 0x6b 

class AssetType(Enum):
    Common = 0x00
    Character = 0x01
    Stage = 0x03

class CharacterIndex(Enum):
    Player = 0x00
    Opponent = 0x01

class Hand(Enum):
    Left = 0x00
    Right = 0x01

class MeterType(Enum):
    HP_METER = 0x00
    HP_METER_= 0x01
    SOUL_METER = 0x02
    SOUL_METER_ = 0x03
    GUARD_METER = 0x04
    GUARD_METER_ = 0x05

class MeterAmount(Enum):
    _0 = 0x00
    _12 = 0x01
    _24 = 0x02
    _36 = 0x03

class MeterCalcBase(Enum):
    _120 = 0x00
    _240 = 0x01


class VoiceCategory(Enum):
    Intro_1P = 0x00
    Intro_2P = 0x01
    Character_Specific_Intro = 0x02
    Outro = 0x03
    Character_Specific_Outro = 0x04
    Character_Select = 0x05
    Call = 0x06
    Demo = 0x07
    Generic_Starter = 0x08
    Generic_End_Quip = 0x09
    Generic_Insert = 0x0a
    Generic_Punish = 0x0b
    Generic_Tease = 0x0c
    CE_Startup = 0x0d
    During_CE = 0x0e
    CE_End = 0x0f
    CE_KO = 0x10
    Generic_Finisher = 0x11
    Throw = 0x12
    Character_Specific = 0x13
    Reversal_Edge_Startup = 0x14
    Reversal_Edge_Parry = 0x15
    Reversal_Edge_Quote = 0x16
    Reversal_Edge_Deflect = 0x17
    Reversal_Edge_Blocked = 0x18
    Reversal_Edge_Lethal_Hit = 0x19
    Reversal_Edge_Evade = 0x1a
    Reversal_Edge_Low_Time = 0x1b
    Soul_Charge = 0x1c
    Decisive = 0x1d
    Laugh = 0x1e
    Guard_Impact_Fail = 0x1f
    Guard_Impact_Fail_Low_HP = 0x20
    Ukemi = 0x21
    Ukemi_Low_HP = 0x22
    Guard_Crush = 0x23
    Taunt = 0x24
    Time_Out = 0x25
    Light_Attack = 0x26
    Medium_Attack = 0x27
    Heavy_Attack = 0x28
    Block = 0x29
    Light_Hurt = 0x2a
    Medium_Hurt = 0x2b
    Heavy_Hurt = 0x2c
    Special_Hurt_1 = 0x2d
    _Hurt_2 = 0x2e
    Guard_Hurt = 0x2f
    Wall_Hit = 0x30
    Drain = 0x31
    Quake = 0x32
    Dizziness = 0x33
    Death_Cry = 0x34


class RandomVoiceCategory(Enum):
    Light_Hurt = 0x00
    Medium_Hurt =0x01
    Light_Attack = 0x04
    Medium_Attack = 0x05 
    Heavy_Attack = 0x06
    Light_Ukemi = 0x07
    Heavy_Ukemi= 0x08
    Whiff_Guard_Impact = 0x09
    Whiff_Guard_Impact_2 = 0x0a
    Special_Hurt = 0x0b
    Grunts_1 = 0x0c
    Grunts_2 = 0x0d
    
class FacialExpression(Enum):
    Standard_1 = 0x00
    Standard_2 = 0x01
    Happy = 0x02
    Angry = 0x03
    Sad = 0x04
    In_Pain = 0x05
    Anguished = 0x06
    Smiling = 0x07
    Surprised = 0x08
    Scared = 0x09
    Frustrated = 0x0a
    Eyes_Closed = 0x0b
    Extra_1 = 0x0c
    Extra_2 = 0x0d
    Extra_3 = 0x0e
    Extra_4 = 0x0f
    Extra_5 = 0x10

class AirStunType(Enum):
    None__Allow_AC = 0x00
    Air__Vertical_Spiral = 0x01
    Air__Vertical_Spiral_Bounce = 0x02
    Air__Vertical_Roll = 0x03
    Air__Horizontal_Spiral = 0x04
    Bind__Bounce = 0x05
    Bind__Stun = 0x06
    Bind__Knockback = 0x07
    Air__Horizontal_Roll = 0x08
    Air_Bind__Vertical_Spiral__Disable_Ukemi = 0x09
    Bind__Grounded = 0x0a
    Bind__Long_Grounded_Recovery = 0x0b
    Bind__Vertical_Roll = 0x0c
    Air__Relaunch = 0x0d
    unk__Flip_Forward = 0x0e
    Bind__Pull_Toward = 0x0f
    Short_Bind__Knockback = 0x10
    Air__Faster_Vertical_Roll = 0x11
    Bind__Rolling_Restand = 0x12
    Bind__Knockback_2 = 0x13
    Bind_Grounded__Gets_up = 0x14
    Air_Bind__Vertical_Spiral__Allow_Ukemi = 0x15
    Bind__Inverted_Knockback = 0x16
    None__Disable_AC = 0x17

class LH_Situation(Enum):
    Standing = 0x01
    Crouching = 0x02
    Standing_or_Crouching = 0x03
    Airborne = 0x04
    Standing_or_Airborne = 0x05
    Crouching_or_Airborne = 0x06
    Standing_or_Crouching_or_Airborne = 0x07
    Jumping = 0x0c
    Downed = 0x10
    Guard_Impacted = 0x20
    Determined_from_Character_Value = 0x23

class LH_Condition(Enum):
    Attack_Counter__First_Hit = 0x01
    Attack_Counter__Second_Hit = 0x02
    Attack_Counter = 0x03
    Run_Counter__Side = 0x04
    Run_Counter__Side_or_Attack_Counter__First_Hit = 0x05
    Run_Counter__Side_or_Attack_Counter__Second_Hit = 0x06
    Run_Counter__Side_or_Attack_Counter = 0x07
    Step_Counter__Side = 0x08
    Step_Counter__Side_or_Attack_Counter_First_Hit = 0x09
    Step_Counter__Side_or_Attack_Counter_Second_Hit = 0x0a
    Step_Counter__Side_or_Attack_Counter = 0x0b
    Step_Counter__Side_or_Run_Counter__Side = 0x0c
    Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter_First_Hit = 0x0d
    Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter_Second_Hit = 0x0e
    Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter = 0x0f
    Run_Counter__Back = 0x10
    Run_Counter__Back_or_Attack_Counter_First_Hit = 0x11
    Run_Counter__Back_or_Attack_Counter_Second_Hit = 0x12
    Run_Counter__Back_or_Attack_Counter = 0x13
    Run_Counter__Back_or_Run_Counter__Side = 0x14
    Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter_First_Hit = 0x15
    Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter_Second_Hit = 0x16
    Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter = 0x17
    Run_Counter__Back_or_Step_Counter__Side = 0x18
    Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter__First_Hit = 0x19
    Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter__Second_Hit = 0x1a
    Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter = 0x1b
    Run_Counter = 0x1c
    Run_Counter_or_Attack_Counter__First_Hit = 0x1d
    Run_Counter_or_Attack_Counter__Second_Hit = 0x1e
    Run_Counter_or_Attack_Counter = 0x1f
    Guard_Crush = 0x20
    Guard_Crush_or_Attack_Counter__First_Attack = 0x21
    Guard_Crush_or_Attack_Counter__Second_Attack = 0x22
    Guard_Crush_or_Attack_Counter = 0x23
    Guard_Crush_or_Run_Counter__Side = 0x24
    Guard_Crush_or_Run_Counter__Side_or_Attack_Counter__First_Hit = 0x25
    Guard_Crush_or_Run_Counter__Side_or_Attack_Counter__Second_Hit = 0x26
    Guard_Crush_or_Run_Counter__Side_or_Attack_Counter = 0x27
    Guard_Crush_or_Step_Counter__Side = 0x28
    Guard_Crush_or_Step_Counter__Side_or_Attack_Counter__First_Hit = 0x29
    Guard_Crush_or_Step_Counter__Side_or_Attack_Counter__Second_Hit = 0x2a
    Guard_Crush_or_Step_Counter__Side_or_Attack_Counter = 0x2b
    Guard_Crush_or_Step_Counter__Side_or_Run_Counter__Side = 0x2c
    Guard_Crush_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter__First_Hit = 0x2d
    Guard_Crush_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter__Second_Hit = 0x2e
    Guard_Crush_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter = 0x2f
    Guard_Crush_or_Run_Counter__Back = 0x30
    Guard_Crush_or_Run_Counter__Back_or_Attack_Counter__First_Hit = 0x31
    Guard_Crush_or_Run_Counter__Back_or_Attack_Counter__Second_Hit = 0x32
    Guard_Crush_or_Run_Counter__Back_or_Attack_Counter = 0x33
    Guard_Crush_or_Run_Counter__Back_or_Run_Counter__Side = 0x34
    Guard_Crush_or_Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter__First_Hit = 0x35
    Guard_Crush_or_Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter__Second_Hit = 0x36
    Guard_Crush_or_Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter = 0x37
    Guard_Crush_or_Run_Counter__Back_or_Step_Counter__Side = 0x38
    Guard_Crush_or_Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter__First_Hit = 0x39
    Guard_Crush_or_Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter__Second_Hit = 0x3a
    Guard_Crush_or_Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter = 0x3b
    Guard_Crush_or_Run_Counter = 0x3c
    Guard_Crush_or_Run_Counter_or_Attack_Counter__First_Hit = 0x3d
    Guard_Crush_or_Run_Counter_or_Attack_Counter__Second_Hit = 0x3e
    Guard_Crush_or_Run_Counter_or_Attack_Counter = 0x3f
    Impact_Counter = 0x40
    Impact_Counter_or_Attack_Counter__First_Attack = 0x41
    Impact_Counter_or_Attack_Counter__Second_Attack = 0x42
    Impact_Counter_or_Attack_Counter = 0x43
    Impact_Counter_or_Run_Counter__Side = 0x44
    Impact_Counter_or_Run_Counter__Side_or_Attack_Counter__First_Attack = 0x45
    Impact_Counter_or_Run_Counter__Side_or_Attack_Counter__Second_Attack = 0x46
    Impact_Counter_or_Run_Counter__Side_or_Attack_Counter = 0x47
    Impact_Counter_or_Step_Counter__Side = 0x48
    Impact_Counter_or_Step_Counter__Side_or_Attack_Counter__First_Attack = 0x49
    Impact_Counter_or_Step_Counter__Side_or_Attack_Counter__Second_Attack = 0x4a
    Impact_Counter_or_Step_Counter__Side_or_Attack_Counter = 0x4b
    Impact_Counter_or_Step_Counter__Side_or_Run_Counter__Side = 0x4c
    Impact_Counter_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter__First_Attack = 0x4d
    Impact_Counter_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter__Second_Attack = 0x4e
    Impact_Counter_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter = 0x4f
    Impact_Counter_or_Run_Counter__Back = 0x50
    Impact_Counter_or_Run_Counter__Back_or_Attack_Counter__First_Attack = 0x51
    Impact_Counter_or_Run_Counter__Back_or_Attack_Counter__Second_Attack = 0x52
    Impact_Counter_or_Run_Counter__Back_or_Attack_Counter = 0x53
    Impact_Counter_or_Run_Counter__Back_or_Run_Counter__Side = 0x54
    Impact_Counter_or_Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter__First_Attack = 0x55
    Impact_Counter_or_Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter__Second_Attack = 0x56
    Impact_Counter_or_Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter = 0x57
    Impact_Counter_or_Run_Counter__Back_or_Step_Counter__Side = 0x58
    Impact_Counter_or_Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter__First_Attack = 0x59
    Impact_Counter_or_Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter__Second_Attack = 0x5a
    Impact_Counter_or_Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter = 0x5b
    Impact_Counter_or_Run_Counter__Back_or_Step_Counter__Side_or_Run_Counter__Side = 0x5c
    Impact_Counter_or_Run_Counter__Back_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter__First_Attack = 0x5d
    Impact_Counter_or_Run_Counter__Back_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter__Second_Attack = 0x5e
    Impact_Counter_or_Run_Counter__Back_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter = 0x5f
    Impact_Counter_or_Guard_Crush = 0x60
    Impact_Counter_or_Guard_Crush_or_Attack_Counter__First_Attack = 0x61
    Impact_Counter_or_Guard_Crush_or_Attack_Counter__Second_Attack = 0x62
    Impact_Counter_or_Guard_Crush_or_Attack_Counter = 0x63
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Side = 0x64
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Side_or_Attack_Counter__First_Hit = 0x65
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Side_or_Attack_Counter__Second_Hit = 0x66
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Side_or_Attack_Counter = 0x67
    Impact_Counter_or_Guard_Crush_or_Step_Counter__Side = 0x68
    Impact_Counter_or_Guard_Crush_or_Step_Counter__Side_or_Attack_Counter__First_Hit = 0x69
    Impact_Counter_or_Guard_Crush_or_Step_Counter__Side_or_Attack_Counter__Second_Hit = 0x6a
    Impact_Counter_or_Guard_Crush_or_Step_Counter__Side_or_Attack_Counter = 0x6b
    Impact_Counter_or_Guard_Crush_or_Step_Counter__Side_or_Run_Counter__Side = 0x6c
    Impact_Counter_or_Guard_Crush_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter__First_Hit = 0x6d
    Impact_Counter_or_Guard_Crush_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter__Second_Hit = 0x6e
    Impact_Counter_or_Guard_Crush_or_Step_Counter__Side_or_Run_Counter__Side_or_Attack_Counter = 0x6f
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back = 0x70
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Attack_Counter__First_Hit = 0x71
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Attack_Counter__Second_Hit = 0x72
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Attack_Counter = 0x73
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Run_Counter__Side = 0x74
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter__First_Hit = 0x75
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter__Second_Hit = 0x76
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Run_Counter__Side_or_Attack_Counter = 0x77
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Step_Counter__Side = 0x78
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter__First_Hit = 0x79
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter__Second_Hit = 0x7a
    Impact_Counter_or_Guard_Crush_or_Run_Counter__Back_or_Step_Counter__Side_or_Attack_Counter = 0x7b
    Impact_Counter_or_Guard_Crush_or_Run_Counter = 0x7c
    Impact_Counter_or_Guard_Crush_or_Run_Counter_or_Attack_Counter__First_Hit = 0x7d
    Impact_Counter_or_Guard_Crush_or_Run_Counter_or_Attack_Counter__Second_Hit = 0x7e
    Impact_Counter_or_Guard_Crush_or_Run_Counter_or_Attack_Counter = 0x7f
 

    Counter_Hit = 0x017e
    Opening_After_Opponent_Guard = 0x0200
    Opponent_Missed_Attack = 0x0400
    Opponent_Hit_During_Attack = 0x0402
    Opponent_Missed_Guard_Impact = 0x0441
    Character_Value_Check = 0x077f

class GI_Type(Enum):
    Inward_GI = 0x0146
    Outward_GI_ = 0x0147
    Armor = 0x0148
    Outward_GI = 0x0149
    Revenge = 0x014a
    Clash = 0x014b
    RI_ = 0x014c
    Thrust = 0x014d
    Inward_GI_ = 0x014e
    RI = 0x014f

class AttackLevel(Enum):
    High = 0x0140
    Middle = 0x0141
    Low = 0x0142
    High_and_Middle = 0x0143
    Middle_and_Low = 0x0144
    All = 0x0145

    

class StunOverride(Enum):
    STAND = 0x01
    AIR = 0x02
    ALL = 0x03

class ViewTarget(Enum):
    Opponent = 0x01
    Player = 0x02
    Stage = 0x0a

class OpponentState(Enum):
    Grounded = 0x03
    Airborne = 0x07
    Airborne_ = 0x0f
    Hurt = 0x1b
    Block = 0x2e

class CharacterValue(Enum):
    Soul_Gauge = 0x00
    Guard_Gauge = 0x02
    Stun_Hits_Received = 0x03
    Ring_Out_Voiceline = 0x09
    Soul_Charge = 0x0a
    Guard_Break = 0x0d

class CharacterID(Enum):
    Mitsurugi = 0x01
    Seong_Mina = 0x02
    Taki = 0x03
    Maxi = 0x04
    Voldo = 0x05
    Sophitia = 0x06
    Siegfried = 0x07
    Rock = 0x08
    Hwang = 0x09
    Arthur_SC1 = 0x0a
    Ivy = 0x0b
    Kilik = 0x0c
    Xianghua = 0x0d
    Lizardman = 0x0e
    Yoshimitsu = 0x0f
    Edge_Master = 0x10
    Nightmare = 0x11
    Astaroth = 0x12
    Inferno = 0x13
    Cervantes = 0x14
    Raphael = 0x15
    Talim = 0x16
    Cassandra = 0x17
    Charade = 0x18
    Necrid = 0x19
    Yun_Seong = 0x1a
    Link = 0x1b
    Heihachi = 0x1c
    Spawn = 0x1d
    Lizardmen_SC2 = 0x1e
    Assassin = 0x1f
    Berserker = 0x20
    Setsuka = 0x22
    Tira = 0x23
    Zasalamel = 0x24
    Olcadan = 0x25
    Abyss = 0x26
    Night_Terror = 0x27
    Hilde = 0x28
    Algol = 0x29
    Darth_Vader = 0x2a
    Yoda = 0x2b
    The_Apprentice = 0x2c
    Creation = 0x2d
    Kratos = 0x2e
    Dampierre = 0x2f
    Amy = 0x30
    ZWEI = 0x31
    Viola = 0x32
    Pyrrha = 0x33
    Pyrrha_Omega = 0x34
    Patroklos = 0x35
    Alpha_Patroklos = 0x36
    Natsu = 0x37
    Xiba = 0x38
    Leixia = 0x39
    Aeon = 0x3a
    Yoshimitsu2 = 0x3b
    Elysium = 0x3c
    Master_Kilik = 0x3d
    Boss_Astaroth = 0x3e
    Boss_Cervantes = 0x3f
    Boss_Nightmare_or_Angol_Fear = 0x40
    Devil_Jin_or_Kamikirimusi_or_Miser = 0x41
    Ezio_Auditore_or_Shura_or_Greed = 0x42
    Ashlotte_or_Arthur = 0x43
    Scheherazade_or_Hwang = 0x44
    Luna = 0x45
    Valeria = 0x46
    Hualin = 0x47
    Girardot = 0x48
    Demuth = 0x4a
    Aurelia = 0x4b
    Chester = 0x4c
    Strife = 0x4d
    Abelia = 0x4e
    Lynette = 0x4f
    Li_Long = 0x51
    Revenant = 0x54
    _2B = 0x60
    Haohmaru = 0x61
    Grøh = 0x62
    Azwel = 0x64
    Geralt = 0x65
    Lesser_Lizardman = 0x66
    Evil_Kilik = 0x67
    Evil_Grøh = 0x68
    Boss_Azwel = 0x69
    Conduit = 0x6a






class CC(Enum): #Cancel codes for the cancel block, mostly we expect (CC XX XX CC XX XX ...) where CC is the cancel codes and XX is the variable provided to them
    UNK = 0x9999

    START = 0x01 #begins every block(?)
    END = 0x02  # this byte ends the block

    EXE_25 = 0x25 #all EXE blocks have the seecond argument as the number of instructions since the last non 8b/89 block (mostly true)
    EXE_19 = 0x19 #very common in neutral blocks
    EXE_A5 = 0xA5
    EXE_12 = 0x12 # Increase variable value by 1.
    EXE_13 = 0x13 # Decrease variable value by 1.

    ARG_89 = 0x89 #the ARG blocks provide arguments to the EXE blocks
    ARG_8B = 0x8b
    ARG_8A = 0x8a #read var value

    PEN_2A = 0x2A #the variables for these blocks stay the same or increase (although they may start in the middle of the block and 'wrap' around to the top)
    PEN_28 = 0x28
    PEN_29 = 0x29

    RETURN_00 = 0x00
    RETURN_03 = 0x03
    RETURN_04 = 0x04
    RETURN_05 = 0x05
    RETURN_07 = 0x07
    RETURN_08 = 0x08
    RETURN_0b = 0x0b
    RETURN_0d = 0x0d
    RETURN_0e = 0x0e
    RETURN_0f = 0x0f
    RETURN_10 = 0x10
    RETURN_12 = 0x12
    RETURN_13 = 0x13
    RETURN_14 = 0x14
    RETURN_1a = 0x1a
    RETURN_1b = 0x1b
    RETURN_1c = 0x1c
    RETURN_1e = 0x1e
    RETURN_23 = 0x23
    RETURN_32 = 0x32
    RETURN_42 = 0x42
    RETURN_4c = 0x4c
    RETURN_4d = 0x4d
    RETURN_5c = 0x5c
    RETURN_5d = 0x5d
    RETURN_61 = 0x61
    RETURN_68 = 0x68
    RETURN_6b = 0x6b
    RETURN_74 = 0x74
    RETURN_77 = 0x77
    RETURN_78 = 0x78
    RETURN_7a = 0x7a
    RETURN_7e = 0x7e
    RETURN_88 = 0x88
    RETURN_8c = 0x8c
    RETURN_8d = 0x8d
    RETURN_8e = 0x8e
    RETURN_8f = 0x8f
    RETURN_90 = 0x90
    RETURN_91 = 0x91
    RETURN_92 = 0x92
    RETURN_94 = 0x94
    RETURN_95 = 0x95
    RETURN_96 = 0x96
    RETURN_98 = 0x98
    RETURN_99 = 0x99
    RETURN_9e = 0x9e
    RETURN_9f = 0x9f
    RETURN_a0 = 0xa0
    RETURN_a1 = 0xa1
    RETURN_a2 = 0xa2
    RETURN_a3 = 0xa3
    RETURN_a4 = 0xa4
    RETURN_ab = 0xab
    RETURN_ac = 0xac
    RETURN_ad = 0xad
    RETURN_ae = 0xae
    RETURN_af = 0xaf
    RETURN_b1 = 0xb1
    RETURN_b3 = 0xb3
    RETURN_f0 = 0xf0
    RETURN_fb = 0xfb



