# Online Ballot Regulator
The Online Ballot Regulator deals with adding *verified* voter addresses to the ballot contract for which they are entitled to vote on. This node also holds the ballotID ascociated with a voterID so that it can be requested/retrieved later.

## Online Registration
- [ ] Registers a voterAddress to a specific ballot contract.
- [ ] Funds the voterAddress with enough ether to vote.

## Voting
- [ ] Upon request, retrieves the ballot contract asocoiated with a voterID


# TODO
- [ ] SSL twisted connections

# manual run
docker run -it -p 5434:5434 \
    --env-file=./bin/Variables.env
    --workdir=/usr/src/onlineballotregulator/ \
    -v ${PWD}:/usr/src/onlineballotregulator/ \
    -v ${PWD}/../ethereumDB:/usr/src/ethereumDB/ \
    4_test bash