const notFound = (req, res, next) => {
  const error = new Error(`Not found - ${req.originalURL}`);
  res.status(404);
  next(error);
};

const errorHandler = (err, req, res, next) => {
  console.log("Hi")
  const statusCode = res.status.Code === 200 ? 500 : res.status.Code;
  res.status(statusCode);
  res.send("Error")
};

module.exports = { notFound, errorHandler };
