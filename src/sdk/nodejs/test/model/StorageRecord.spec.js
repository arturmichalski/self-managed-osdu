/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.22
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.SelfManagedOsdu);
  }
}(this, function(expect, SelfManagedOsdu) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('StorageRecord', function() {
      beforeEach(function() {
        instance = new SelfManagedOsdu.StorageRecord();
      });

      it('should create an instance of StorageRecord', function() {
        // TODO: update the code to test StorageRecord
        expect(instance).to.be.a(SelfManagedOsdu.StorageRecord);
      });

      it('should have the property id (base name: "id")', function() {
        // TODO: update the code to test the property id
        expect(instance).to.have.property('id');
        // expect(instance.id).to.be(expectedValueLiteral);
      });

      it('should have the property kind (base name: "kind")', function() {
        // TODO: update the code to test the property kind
        expect(instance).to.have.property('kind');
        // expect(instance.kind).to.be(expectedValueLiteral);
      });

      it('should have the property acl (base name: "acl")', function() {
        // TODO: update the code to test the property acl
        expect(instance).to.have.property('acl');
        // expect(instance.acl).to.be(expectedValueLiteral);
      });

      it('should have the property legal (base name: "legal")', function() {
        // TODO: update the code to test the property legal
        expect(instance).to.have.property('legal');
        // expect(instance.legal).to.be(expectedValueLiteral);
      });

      it('should have the property data (base name: "data")', function() {
        // TODO: update the code to test the property data
        expect(instance).to.have.property('data');
        // expect(instance.data).to.be(expectedValueLiteral);
      });

      it('should have the property history (base name: "history")', function() {
        // TODO: update the code to test the property history
        expect(instance).to.have.property('history');
        // expect(instance.history).to.be(expectedValueLiteral);
      });

    });
  });

}));
