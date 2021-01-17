# Online Account Verifier
The `Online Account Verifier` has the job of only allowing valid (as determined by the `External Voter Registration`) voters to be assingned to their respective ballot contracts.

## Pre Election Registration
- [ ] Receive voterID of a verified voter & their ascociated ballot information.

## Online Registration
- [ ] Signs the blind token *iff* the voterID has been received & its the first time we've seen this token.
- [ ] Checks if the requested voterAddress & signed token are valid then requests `Online Ballot Regulator` to add them to the ballot contract.


# manual run
docker run -it -p 5435:5435 \
    --env-file=./bin/Variables.env \
    --workdir=/usr/src/onlineaccountverifier/ \
    -v ${PWD}:/usr/src/onlineaccountverifier/ \
    -v ${PWD}/../ethereumDB:/usr/src/ethereumDB/ \
    3_test bash