var ColumbusToken = artifacts.require("./ColumbusToken.sol");

module.exports = function(deployer) {
  deployer.deploy(ColumbusToken);
};
