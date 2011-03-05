require './helper'

class Paginator
  extend PaginateSimple
end

describe PaginateSimple do
  before do
    Paginator.config :total => 100 , :page => 1, :per_page => 10
  end
  
  it "should be configured properly" do
    Paginator.total.should eql(100)
    Paginator.current_page.should eql(1)
    Paginator.per_page.should eql(10)
  end

  it "should provide the correct number of pages" do
    Paginator.num_of_pages.should eql(10)
  end
  
  it "should answer to has_next_page? correctly" do
    Paginator.should have_next_page
    Paginator.current_page = 10
    Paginator.should_not have_next_page
  end
  
  it "should answer to has_previous_page? correctly" do
    Paginator.should_not have_previous_page
    Paginator.current_page = 2
    Paginator.should have_next_page
  end
  
  it "should return pages as iterator" do
    Paginator.pages.should respond_to(:each)
    Paginator.current_page = 1
    Paginator.total = 0
    Paginator.pages.should respond_to(:each)
  end
  
  it "should return correct num of pages" do
    Paginator.per_page = 3
    Paginator.total = 10
    Paginator.should have(4).pages
    
    Paginator.current_page = 1
    Paginator.total = 0
    Paginator.should have(0).pages
  end
  
  it "should provide offset" do
    Paginator.current_page = 2
    Paginator.offset.should eql(10)
  end
  
  it "should return next page or nil otherwise" do
    Paginator.current_page = 4
    Paginator.should have_next_page
    Paginator.next_page.should  eql(5)
    
    Paginator.current_page = 10
    Paginator.should_not have_next_page
    Paginator.next_page.should be_nil
  end
  
  it "should return previous page or nil otherwise" do
    Paginator.current_page = 2
    Paginator.should have_previous_page
    Paginator.previous_page.should eql(1)
    
    Paginator.current_page = 1
    Paginator.should_not have_previous_page
    Paginator.previous_page.should be_nil
  end
  
  it "should raise ArgumentError on negative current_page" do
    lambda { Paginator.current_page = -1 }.should raise_error(ArgumentError)
  end
  
  it "should raise ArgumentError on negative total" do
    lambda { Paginator.total = -1 }.should raise_error(ArgumentError)
  end

end
