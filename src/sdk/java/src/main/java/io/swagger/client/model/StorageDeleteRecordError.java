/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * Delete Records Response Body
 */
@ApiModel(description = "Delete Records Response Body")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2022-01-06T20:30:18.662Z")
public class StorageDeleteRecordError {
  @SerializedName("notDeletedRecordId")
  private String notDeletedRecordId = null;

  @SerializedName("message")
  private String message = null;

  public StorageDeleteRecordError notDeletedRecordId(String notDeletedRecordId) {
    this.notDeletedRecordId = notDeletedRecordId;
    return this;
  }

   /**
   * Record id which wasn&#39;t deleted successfully.
   * @return notDeletedRecordId
  **/
  @ApiModelProperty(example = "common:welldb:123456", value = "Record id which wasn't deleted successfully.")
  public String getNotDeletedRecordId() {
    return notDeletedRecordId;
  }

  public void setNotDeletedRecordId(String notDeletedRecordId) {
    this.notDeletedRecordId = notDeletedRecordId;
  }

  public StorageDeleteRecordError message(String message) {
    this.message = message;
    return this;
  }

   /**
   * Brief description of the cause why record wasn&#39;t delete
   * @return message
  **/
  @ApiModelProperty(example = "Record with id 'common:welldb:123456' not found", value = "Brief description of the cause why record wasn't delete")
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StorageDeleteRecordError storageDeleteRecordError = (StorageDeleteRecordError) o;
    return Objects.equals(this.notDeletedRecordId, storageDeleteRecordError.notDeletedRecordId) &&
        Objects.equals(this.message, storageDeleteRecordError.message);
  }

  @Override
  public int hashCode() {
    return Objects.hash(notDeletedRecordId, message);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StorageDeleteRecordError {\n");
    
    sb.append("    notDeletedRecordId: ").append(toIndentedString(notDeletedRecordId)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

