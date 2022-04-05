import { PrismaClient } from "@prisma/client";

export const prisma = new PrismaClient();

export const signupController = async (req, res) => {
  try {
    const { name, email, password } = req.body;

    // check if user exists
    const user = await prisma.user.findUnique({
      where: {
        email: email,
      },
    });
    if (user) return res.status(409).send("email already in use.");

    // create new user
    const newUser = await prisma.user.create({
      data: {
        name: name,
        email: email,
        password: password,
      },
    });
    return newUser;
  } catch (err) {
    return res.status(500).send("Error occured. Please try again");
  }
};
