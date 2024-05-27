CREATE TABLE Cars (
	Make nvarchar(100),
	Model nvarchar(200),
	Type nvarchar(100),
	Origin nvarchar(100),
	DriveTrain nvarchar(100),
	Length decimal(18,0)
)


SELECT distinct(Make) FROM [dbo].[Cars]

SELECT COUNT(*) FROM [dbo].[Cars]