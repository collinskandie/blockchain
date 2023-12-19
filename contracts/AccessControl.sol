pragma solidity ^0.8.0;

contract RBAC {
    mapping(address => string) public roles;

    modifier onlyAdmin() {
        require(keccak256(bytes(roles[msg.sender])) == keccak256(bytes("Admin")), "Permission denied");
        _;
    }

    function grantRole(address user, string memory role) public onlyAdmin {
        roles[user] = role;
    }

    function hasPermission(address user, string memory permission) public view returns (bool) {
        // Implement permission check logic
        return true;
    }
}
