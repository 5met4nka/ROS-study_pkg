study_pkg::Poly srv;
srv.request.x = 5;

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_client");
  if (argc != 3)
  {
    ROS_INFO("usage: add_two_ints_client X Y");
    return 1;
  }

  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<study_pkg::Poly>("poly");
  beginner_tutorials::Poly srv;
  srv.request.x = atoll(argv[1]);

  if (client.call(srv))
  {
    ROS_INFO("Poly: %ld", (long int)srv.response.y);
  }
  else
  {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }
}