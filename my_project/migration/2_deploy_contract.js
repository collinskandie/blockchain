// 2_deploy_contract.js
const AccessControl = artifacts.require("AccessControl");

module.exports = function (deployer) {
  deployer.deploy(AccessControl);
};
