########################################################
#                 ###### ###### ######                 #
#                 #    # #    #      #                 #
#                 ###### ###### ######                 #
#                 #      #    #      #                 #
#                 #      #    # ######                 #
########################################################
#                                                      #
#  By    : Walimuni Tharindu Mendis, Katie O'Leary,    #
#          Aparna Mishra, Bi Pan                       #
#                                                      #
########################################################

PY := python3

.PHONY: clean

openhash: openhash.py
	chmod 755 $^
	$(PY) $^

closedhash: closedhash.py
	@chmod 755 $^
	$(PY) $^

bst: bst.py
	@chmod 755 .
	$(PY) $^

dijkstra2: 
	@chmod 755 dijsktra2.py 
	@python dijsktra2.py

mergelists: mergelists.py
	@chmod 755 .
	$(PY) $^

listconcat: listconcat.py
	@chmod 755 .
	$(PY) $^

levelorder: levelorder.py
	@chmod 755 .
	$(PY) $^

traversalconvert: traversalconvert.py
	@chmod 755 .
	$(PY) $^

preorder: preorder.py
	@chmod 755 .
	$(PY) $^ "* + 2 3 + 4 5"

postorder: postorder.py
	@chmod 755 .
	$(PY) $^ "5 7 + 6 2 -  *"

clean:
	@\rm -f *.pyc
