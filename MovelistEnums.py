from enum import Enum


def enum_has_value(cls, value):
    return any(value == item.value for item in cls)
def name_from_enum(cls, value, replace_char = " ", format = False, slice = False, slice_index = 0):
    try:
        if enum_has_value(cls, value):
            result = cls(value).name
            if slice:
                result = result.split("_")[slice_index]
            if format:
                result = result.capitalize()
            
            return f'{result.replace("_", replace_char)}'
        else:
            return value
            

    
    except:
        return value

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

    B_K = 0x0600
    A_B = 0x0300
    A_G = 0x0900
    B_G = 0x0a00
    K_G = 0x0C00

    A_B_K = 0x0700

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


   

class InputType(Enum):
    Press = 0x06
    Hold = 0x20

    Direction_PRESS = 0x13AF
    Direction_HOLD= 0x13AE
    Direction_ALT = 0x0002
    No_SC_Press =0x8f #for when you're not in soul charge???


    OnContact = 0x0B #counter hit uses the same code signature but are about 3x as long so the counterhit part must be in there somewhere

    DoubleTap = 0x2C

    #PressDown = 0x13af /0x13ae ??
    #PressBack =  0x0002 /0x1002 ??
    #0x0120 #geralt, super?? + hold button

class SpecialState(Enum):
    TECH_CROUCH = 0x02
    TECH_JUMP = 0x04
    TECH_COUNTER = 0x2b

class AssetType(Enum):
    Common = 0x00
    Character = 0x01
    Stage = 0x03


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
    No_Stun = 0x00

class StunOverride(Enum):
    STAND = 0x01
    AIR = 0x02
    ALL = 0x03

class ViewTarget(Enum):
    Opponent = 0x01
    Player = 0x02
    Stage = 0x0a

class OpponentState(Enum):
    Hurt = 0x1b
    Block = 0x2e

class CharacterValue(Enum):
    Soul_Charge = 0x0a

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
    Vader = 0x2a
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
    Boss_Nightmare = 0x40
    Devil_Jin = 0x41
    Guest1 = 0x42
    Guest2 = 0x43
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
    EXE_13 = 0x13 #very rare, yoshimitsu only???

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



