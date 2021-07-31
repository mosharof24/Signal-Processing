%% no of samples
i = -20:20;

%% unit step 
x = zeros(1,length(i));
x(i>=0) = 1;
subplot(3,1,1)
stem(i,x,"fill");
title("unit step");
xlabel("number of samples"); ylabel("amplitude");

%% impulse 
x = zeros(1,length(i));
x(i == 0) = 1;
subplot(3,1,2)
stem(i,x,"fill","b--");title("impulse");
xlabel("sample");ylabel("amplitude");
grid on;

%% ramp
x = zeros(1,length(i));
x(i>=0) = i(i>=0);
subplot(3,1,3)
stem(i,x,"fill","r*");title("ramp");
xlabel("no of sample");ylabel("amplitude");
grid on;