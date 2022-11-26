####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### sql para crear la tabla ubica_vehicle
CREATE TABLE ApiMetroBus.ubica_vehicle (
  id INT auto_increment primary key NOT NULL,
  date_updated varchar(20) NULL,
  
  vehicle_id varchar(5) NULL,
  vehicle_label varchar(4) NULL,
  vehicle_current_status varchar(2) NULL,

  position_latitude varchar(20) NULL,
  position_longitude varchar(20) NULL,
  geographic_point varchar(28) NULL,
  position_speed varchar(3) NULL,
  position_odometer varchar(5) NULL,
  
  trip_schedule_relationship varchar(2) NULL,
  trip_id varchar(8) NULL,
  trip_start_date varchar(8) NULL,
  trip_route_id varchar(4) NULL,
  
  alcaldia_cdmx varchar(255) NULL,
  
  created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  modified_date DATETIME
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_0900_ai_ci;

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------

