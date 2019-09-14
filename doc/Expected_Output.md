# Expected output

This file illustrates what your program's output might look like under various conditions.  You are not required to make your menus or messages match mine, except where such details are spelled out in the [Instructions](Instructions.md).

In the following examples lines beginning with a '$' represent the command typed into the shell. When you run the same command you should not copy the '$'.


## The trivial case: rotation by 0

    $ python src/caesar.py

    Pnrfne Pvcure!

    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/rot0.txt
    Rotation distance (0-25, or 'all')> 0

    ====================================
    data/rot0.txt rotated by 0 positions
    ====================================
    Make it work first before you make it work fast.

    Bruce Whiteside
    Woodridge, Illinois


    P)rocess a file
    E)xit
    ?> e


## Rotation by 5

    $ python src/caesar.py

    Pnrfne Pvcure!

    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/rot5.txt
    Rotation distance (0-25, or 'all')> 5

    ====================================
    data/rot5.txt rotated by 5 positions
    ====================================
    Dro psbcd cdoz sx pshsxq k lbyuox zbyqbkw sc qoddsxq sd dy pksv bozokdklvi.

    Dyw Nepp
    Lovv Vklc


    P)rocess a file
    E)xit
    ?> e


## Rotation by 21 - you cracked the code! (5 + 21 = 26)

    $ python src/caesar.py

    Pnrfne Pvcure!

    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/rot5.txt
    Rotation distance (0-25, or 'all')> 21

    =====================================
    data/rot5.txt rotated by 21 positions
    =====================================
    The first step in fixing a broken program is getting it to fail repeatably.

    Tom Duff
    Bell Labs


    P)rocess a file
    E)xit
    ?> e


## Math is hard. Let's go shopping!

    $ python src/caesar.py

    Pnrfne Pvcure!

    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/rot8.txt
    Rotation distance (0-25, or 'all')> all

    =====================================
    data/rot8.txt rotated by 0 positions
    =====================================
    Epmv qv lwcjb, cam jzcbm nwzkm.

    Smv Bpwuxawv
    Jmtt Tija


    =====================================
    data/rot8.txt rotated by 1 positions
    =====================================
    Fqnw rw mxdkc, dbn kadcn oxaln.

    Tnw Cqxvybxw
    Knuu Ujkb


    =====================================
    data/rot8.txt rotated by 2 positions
    =====================================
    Grox sx nyeld, eco lbedo pybmo.

    Uox Drywzcyx
    Lovv Vklc


    =====================================
    data/rot8.txt rotated by 3 positions
    =====================================
    Hspy ty ozfme, fdp mcfep qzcnp.

    Vpy Eszxadzy
    Mpww Wlmd


    =====================================
    data/rot8.txt rotated by 4 positions
    =====================================
    Itqz uz pagnf, geq ndgfq radoq.

    Wqz Ftaybeaz
    Nqxx Xmne


    =====================================
    data/rot8.txt rotated by 5 positions
    =====================================
    Jura va qbhog, hfr oehgr sbepr.

    Xra Gubzcfba
    Oryy Ynof


    =====================================
    data/rot8.txt rotated by 6 positions
    =====================================
    Kvsb wb rciph, igs pfihs tcfqs.

    Ysb Hvcadgcb
    Pszz Zopg


    =====================================
    data/rot8.txt rotated by 7 positions
    =====================================
    Lwtc xc sdjqi, jht qgjit udgrt.

    Ztc Iwdbehdc
    Qtaa Apqh


    =====================================
    data/rot8.txt rotated by 8 positions
    =====================================
    Mxud yd tekrj, kiu rhkju vehsu.

    Aud Jxecfied
    Rubb Bqri


    =====================================
    data/rot8.txt rotated by 9 positions
    =====================================
    Nyve ze uflsk, ljv silkv wfitv.

    Bve Kyfdgjfe
    Svcc Crsj


    =====================================
    data/rot8.txt rotated by 10 positions
    =====================================
    Ozwf af vgmtl, mkw tjmlw xgjuw.

    Cwf Lzgehkgf
    Twdd Dstk


    =====================================
    data/rot8.txt rotated by 11 positions
    =====================================
    Paxg bg whnum, nlx uknmx yhkvx.

    Dxg Mahfilhg
    Uxee Etul


    =====================================
    data/rot8.txt rotated by 12 positions
    =====================================
    Qbyh ch xiovn, omy vlony zilwy.

    Eyh Nbigjmih
    Vyff Fuvm


    =====================================
    data/rot8.txt rotated by 13 positions
    =====================================
    Rczi di yjpwo, pnz wmpoz ajmxz.

    Fzi Ocjhknji
    Wzgg Gvwn


    =====================================
    data/rot8.txt rotated by 14 positions
    =====================================
    Sdaj ej zkqxp, qoa xnqpa bknya.

    Gaj Pdkilokj
    Xahh Hwxo


    =====================================
    data/rot8.txt rotated by 15 positions
    =====================================
    Tebk fk alryq, rpb yorqb clozb.

    Hbk Qeljmplk
    Ybii Ixyp


    =====================================
    data/rot8.txt rotated by 16 positions
    =====================================
    Ufcl gl bmszr, sqc zpsrc dmpac.

    Icl Rfmknqml
    Zcjj Jyzq


    =====================================
    data/rot8.txt rotated by 17 positions
    =====================================
    Vgdm hm cntas, trd aqtsd enqbd.

    Jdm Sgnlornm
    Adkk Kzar


    =====================================
    data/rot8.txt rotated by 18 positions
    =====================================
    When in doubt, use brute force.

    Ken Thompson
    Bell Labs


    =====================================
    data/rot8.txt rotated by 19 positions
    =====================================
    Xifo jo epvcu, vtf csvuf gpsdf.

    Lfo Uipnqtpo
    Cfmm Mbct


    =====================================
    data/rot8.txt rotated by 20 positions
    =====================================
    Yjgp kp fqwdv, wug dtwvg hqteg.

    Mgp Vjqoruqp
    Dgnn Ncdu


    =====================================
    data/rot8.txt rotated by 21 positions
    =====================================
    Zkhq lq grxew, xvh euxwh irufh.

    Nhq Wkrpsvrq
    Ehoo Odev


    =====================================
    data/rot8.txt rotated by 22 positions
    =====================================
    Alir mr hsyfx, ywi fvyxi jsvgi.

    Oir Xlsqtwsr
    Fipp Pefw


    =====================================
    data/rot8.txt rotated by 23 positions
    =====================================
    Bmjs ns itzgy, zxj gwzyj ktwhj.

    Pjs Ymtruxts
    Gjqq Qfgx


    =====================================
    data/rot8.txt rotated by 24 positions
    =====================================
    Cnkt ot juahz, ayk hxazk luxik.

    Qkt Znusvyut
    Hkrr Rghy


    =====================================
    data/rot8.txt rotated by 25 positions
    =====================================

    Dolu pu kvbia, bzl iybal mvyjl.

    Rlu Aovtwzvu
    Ilss Shiz


    P)rocess a file
    E)xit
    ?> e



## The user provides an invalid option at the main menu

*Note to computer nerds: don't act like this in social situations; this is not
considered proper ettiquete around humans.*

    $ python src/caesar.py

    Pnrfne Pvcure!

    P)rocess a file
    E)xit
    ?> No

    P)rocess a file
    E)xit
    ?> Stop following me

    P)rocess a file
    E)xit
    ?> Quit

    P)rocess a file
    E)xit
    ?> e



## The user specifies a non-existent or inaccessible file

    $ python src/caesar.py

    Pnrfne Pvcure!

    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/NO_SUCH_FILE.txt
    ERROR! This file does not exist or cannot be opened!


    P)rocess a file
    E)xit
    ?> p



## Ensure that an integer falls between 0 and 25

    $ python src/caesar.py

    Pnrfne Pvcure!

    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/rot0.txt
    Rotation distance (0-25, or 'all')> 256
    ERROR! Invalid rotation distance


    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/rot0.txt
    Rotation distance (0-25, or 'all')> 26
    ERROR! Invalid rotation distance


    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/rot0.txt
    Rotation distance (0-25, or 'all')> -1
    ERROR! Invalid rotation distance


    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/rot0.txt
    Rotation distance (0-25, or 'all')> lolwut
    ERROR! Invalid rotation distance


    P)rocess a file
    E)xit
    ?> p

    Enter the name of a file> data/rot0.txt
    Rotation distance (0-25, or 'all')> 0

    ====================================
    data/rot0.txt rotated by 0 positions
    ====================================
    Make it work first before you make it work fast.

    Bruce Whiteside
    Woodridge, Illinois


    P)rocess a file
    E)xit
    ?> e
