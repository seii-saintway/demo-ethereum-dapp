var Array256Lib = artifacts.require("Array256Lib");
var strings = artifacts.require("strings");
var Mecenas = artifacts.require("Mecenas");
var BadgesLedger = artifacts.require("BadgesLedger");

// Owner content creator params
var nickname = web3.utils.fromAscii('kartojal')
var description = "Welcome to Mecenas dApp! You can support the development of Mecenas with your subscription. With a bit of support we could pay an external audit and improve the current implemetation. Every subscriptor will be added to the BACKERS.md file, and Platinum subscriptions will be shown in the main README.md and at the bottom of the webpage."
// IPFS Hash to my profile pic
var ipfsAvatar = "Qme9gQBdV8EYhugNQ2wxgiXVCFTQr7trYQCpVNktsgZemE";

module.exports = function(deployer) {
  var mecenas, ledger;
  deployer.deploy(Array256Lib, { overwrite: false});
  deployer.deploy(strings, { overwrite: false});
  deployer.link(Array256Lib, Mecenas);
  deployer.link(strings, Mecenas);
  
  deployer
  .then(function() {
    return deployer.deploy(BadgesLedger);
  })
  .then(function() {
    return deployer.deploy(Mecenas);
  })
  .then(async function() {
    console.log('\n');
    console.trace();

    console.log('\ntypeof Mecenas:', typeof Mecenas);
    console.log('Mecenas.address:', Mecenas.address);
    mecenas = await Mecenas.at(Mecenas.address);
    console.log('typeof mecenas:', typeof mecenas);
//     console.log('mecenas', mecenas);

    console.log('\ntypeof BadgesLedger:', typeof BadgesLedger);
    console.log('BadgesLedger.address:', BadgesLedger.address);
    ledger = await BadgesLedger.at(BadgesLedger.address);
    console.log('typeof ledger:', typeof ledger);
//     console.log('ledger', ledger);

    console.log('\nmecenas.setBadgesLedgerContract:', mecenas.setBadgesLedgerContract);
    mecenas.setBadgesLedgerContract(BadgesLedger.address);

    console.log('\nledger.setMinterAddress:', ledger.setMinterAddress);
    ledger.setMinterAddress(Mecenas.address);

    // Creator first content creator, the same owner of the contract
    mecenas.contentCreatorFactory(nickname, description, ipfsAvatar);

    console.log('\n');
  });

};
