import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

const signupController = async (req, res) => {
  try {
    const { name, email, password } = req.body;

    // check if user exists
    const user = await prisma.user.findUnique({
      where: {
        email: email,
      },
    });
    if (user) return res.status(409).send("email already in use.");
  } catch (err) {
    return res.status(500).send("Error occured. Please try again");
  }
};
