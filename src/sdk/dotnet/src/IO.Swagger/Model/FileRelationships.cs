/* 
 * self-managed-osdu
 *
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// All relationships from this entity.
    /// </summary>
    [DataContract]
    public partial class FileRelationships :  IEquatable<FileRelationships>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="FileRelationships" /> class.
        /// </summary>
        /// <param name="parentEntity">parentEntity.</param>
        /// <param name="relatedItems">relatedItems.</param>
        public FileRelationships(FileToOneRelationship parentEntity = default(FileToOneRelationship), FileToManyRelationship relatedItems = default(FileToManyRelationship))
        {
            this.ParentEntity = parentEntity;
            this.RelatedItems = relatedItems;
        }
        
        /// <summary>
        /// Gets or Sets ParentEntity
        /// </summary>
        [DataMember(Name="parentEntity", EmitDefaultValue=false)]
        public FileToOneRelationship ParentEntity { get; set; }

        /// <summary>
        /// Gets or Sets RelatedItems
        /// </summary>
        [DataMember(Name="relatedItems", EmitDefaultValue=false)]
        public FileToManyRelationship RelatedItems { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class FileRelationships {\n");
            sb.Append("  ParentEntity: ").Append(ParentEntity).Append("\n");
            sb.Append("  RelatedItems: ").Append(RelatedItems).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as FileRelationships);
        }

        /// <summary>
        /// Returns true if FileRelationships instances are equal
        /// </summary>
        /// <param name="input">Instance of FileRelationships to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(FileRelationships input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.ParentEntity == input.ParentEntity ||
                    (this.ParentEntity != null &&
                    this.ParentEntity.Equals(input.ParentEntity))
                ) && 
                (
                    this.RelatedItems == input.RelatedItems ||
                    (this.RelatedItems != null &&
                    this.RelatedItems.Equals(input.RelatedItems))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.ParentEntity != null)
                    hashCode = hashCode * 59 + this.ParentEntity.GetHashCode();
                if (this.RelatedItems != null)
                    hashCode = hashCode * 59 + this.RelatedItems.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}